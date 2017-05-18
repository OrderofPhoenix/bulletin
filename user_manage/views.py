from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm, FindPasswordForm, ModifyPasswordForm, ResetPasswordForm
from .models import User
from utils.Token import Token
import utils.FormValidate as fv
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.
DOMAIN = 'http://127.0.0.1:8000'
SECRET_KEY = '&z7jnf_$o0=wz4ck90otanv$3v&-(pcy7w9%nk7!-$#md36nxr'
token_confirm = Token(SECRET_KEY)

def index(request):
    if request.user.is_authenticated():
        return render(request, 'user_manage/info.html', {'msg': 'Welcome, ' + request.user.username})
    login_form = LoginForm()
    return render(request, 'user_manage/index.html', {'login_form': login_form})

def sign_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            uid = login_form.cleaned_data['uid']
            try:
                if User.objects.get_by_natural_key(uid).is_active == False:
                    return render(request, 'user_manage/info.html', {'msg': 'your account is not activated yet!', 'not_activate': True,
                                                         'uid': uid})
            except ObjectDoesNotExist:
                return render(request, 'user_manage/info.html', {'msg': 'user does not exist!'})

            pwd = login_form.cleaned_data['pwd']
            user = authenticate(username=uid, password=pwd)
            if user is not None:
                login(request, user)
                return render(request, 'user_manage/info.html', {'msg': 'Welcome, ' + uid})
            else:
                return render(request, 'user_manage/info.html', {'msg': 'username or password wrong!'})
        else:
            return render(request, 'user_manage/index.html', {'login_form': login_form})
    else:
        login_form = LoginForm()
        return render(request, 'user_manage/index.html', {'login_form': login_form})

def sign_up(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        uid_list = User.objects.values_list('username', flat=True)
        if reg_form.is_valid():
            uid = reg_form.cleaned_data['uid']
            if uid in uid_list:
                return render(request, 'user_manage/info.html', {'msg': 'user is already exists!'})
            email = reg_form.cleaned_data['email']
            pwd = reg_form.cleaned_data['pwd']
            re_pwd = reg_form.cleaned_data['re_pwd']
            sec_q = reg_form.cleaned_data['sec_q']
            sec_a = reg_form.cleaned_data['sec_a']
            if not fv.is_username_valid(uid):
                return render(request, 'user_manage/info.html', {'msg': 'username format error! NOTE: username should be at least 6 characters including letters, digits, hyphens and underscores and at maximum 20 characters'})
            if pwd != re_pwd:
                return render(request, 'user_manage/info.html', {'msg': 'two passwords do not match!'})
            if not fv.is_password_valid(pwd):
                return render(request, 'user_manage/info.html', {'msg': 'password format error! NOTE: password should be at least 6 characters including letters, digits and symbols and at maximum 20 characters'})
            user = User(username=uid, email=email,
                        security_question=sec_q, security_answer=sec_a,
                        is_active=False)
            user.set_password(pwd)
            user.save()
            return render(request, 'user_manage/info.html', {'msg': 'registration complete!'})
    else:
        reg_form = RegisterForm()
        return render(request, 'user_manage/register.html', {'reg_form': reg_form})

@login_required
def sign_out(request):
    logout(request)
    return redirect('/signin/')

def verify_uid(request):
    if request.method == 'POST':
        uid = request.POST.get('verify_account')
        if User.objects.get(username=uid) is not None:
            user = User.objects.get_by_natural_key(username=uid)
            fp_form = FindPasswordForm()
            return render(request, 'user_manage/find_password.html', {'fp_form': fp_form, 'user': user})
        else:
            return render(request, 'user_manage/info.html', {'msg': 'user does not exist!'})
    else:
        fp_form = FindPasswordForm()
        return render(request, 'user_manage/verify_uid.html', {'fp_form': fp_form})

def find_password(request):
    if request.method == 'POST':
        fp_form = FindPasswordForm(request.POST)
        if fp_form.is_valid():
            sec_a = fp_form.cleaned_data['sec_a']
            username = request.POST.get('username')
            user = User.objects.get_by_natural_key(username)
            if sec_a == user.security_answer:
                rp_form = ResetPasswordForm()
                return render(request, 'user_manage/modify_password.html', {'rp_form': rp_form, 'is_verified': True, 'user': user})
            else:
                return render(request, 'user_manage/info.html', {'msg': 'security answer is not current!'})
        else:
            fp_form = FindPasswordForm()
            return render(request, 'user_manage/find_password.html', {'fp_form': fp_form})
    else:
        fp_form = FindPasswordForm()
        return render(request, 'user_manage/find_password.html', {'fp_form': fp_form})

def modify_password(request):
    if request.method == 'POST' and request.POST.get('type') == 'modify':
        mp_form = ModifyPasswordForm(request.POST)
        if mp_form.is_valid():
            old_pwd = mp_form.cleaned_data['old_pwd']
            pwd = mp_form.cleaned_data['new_pwd']
            re_pwd = mp_form.cleaned_data['re_pwd']
            user = request.user.check_password(old_pwd)
            if user:
                if pwd == re_pwd:
                    request.user.set_password(pwd)
                    request.user.save()
                    return render(request, 'user_manage/info.html', {'msg': 'password has been successfully modified!'})
                else:
                    return render(request, 'user_manage/info.html', {'msg': 'two passwords do not match!'})
            else:
                return render(request, 'user_manage/info.html', {'msg': 'old password wrong!'})
        else:
            mp_form = ModifyPasswordForm()
            return render(request, 'modify_password.html', {'mp_form': mp_form})
    elif request.method == 'POST' and request.POST.get('type') == 'reset':
        rp_form = ResetPasswordForm(request.POST)
        if rp_form.is_valid():
            pwd = rp_form.cleaned_data['new_pwd']
            re_pwd = rp_form.cleaned_data['re_pwd']
            user = User.objects.get_by_natural_key(request.POST.get('username'))
            if pwd == re_pwd:
                user.set_password(pwd)
                user.save()
                return render(request, 'user_manage/info.html', {'msg': 'your password has successfully reset'})
            else:
                return render(request, 'user_manage/info.html', {'msg': 'two passwords do not match!'})
        else:
            user = User.objects.get_by_natural_key(request.POST.get('username'))
            rp_form = ResetPasswordForm()
            return render(request, 'user_manage/modify_password.html', {'rp_form': rp_form, 'is_verified': True, 'user': user})
    else:
        mp_form = ModifyPasswordForm()
        return render(request, 'user_manage/modify_password.html', {'mp_form': mp_form})

@login_required
def self_profile(request):
    if request.user is None:
        return redirect('/signin/')
    else:
        user = User.objects.get_by_natural_key(request.user.username)
        return render(request, 'user_manage/info.html', {'msg': 'PROFILE\nusername:' + user.username
                                                    + '\nemail:' + user.email
                                                    + '\nSecQ:' + user.security_question
                                                    + '\nSecA:' + user.security_answer, 'user': user})



#User activation module
def activate_mail_send(request, username):
    user = User.objects.get_by_natural_key(username)
    email = user.email
    token = token_confirm.generate_validate_token(username)
    message = 'To activate your account go to '+ DOMAIN +'/activate='+token
    send_mail(subject='Account Activation', message=message,from_email='team_phoenix@outlook.com' ,recipient_list=[email])
    return render(request, 'user_manage/info.html', {'msg': 'activation has been sent!'})

def activate(request, token):
    try:
        username = token_confirm.confirm_validate_token(token)
    except:
        return render(request, 'user_manage/info.html', {'msg': 'verify link has expired!'})

    try:
        user = User.objects.get_by_natural_key(username)
    except:
        return render(request, 'user_manage/info.html', {'msg': 'user you request is not exist!'})
    user.is_active=True
    user.save()
    return render(request, 'user_manage/info.html', {'msg': 'you have successfully activated your account!'})





