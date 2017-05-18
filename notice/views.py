from django.shortcuts import render, redirect
from .models import Notice, Comment, Bulletin
from .forms import NoticeForm, BulletinForm, CommentForm
from user_manage.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def browse_bulletins(request):
    bulletin_list = Bulletin.objects.all()
    user = User.objects.get_by_natural_key(request.user.username)
    followed_bulletins = Bulletin.objects.filter(follower=user)
    return render(request, 'notice/browse_bulletins.html', {'bulletin_list': bulletin_list,
                                                            'followed_bulletins': followed_bulletins})

@login_required
def get_notice_list(request):
    notice_list = Notice.object.all()
    return render(request, 'notice/browse_bulletins.html', {'notice_list': notice_list})

@login_required
def browse_notices_by_bulletin(request, bid):
    bulletin = Bulletin.objects.get(pk=bid)
    notice_list = Notice.objects.filter(bulletin=bulletin)
    return render(request, 'notice/browse_notices.html', {'notice_list': notice_list})

@login_required
def get_notice_detail_and_comment(request, nid):
    if request.method == 'GET':
        c_form = CommentForm()
        notice = Notice.objects.get(pk=nid)
        comment_list = Comment.objects.filter(belong_to=notice)
        return render(request, 'notice/notice_detail.html', {'notice': notice, 'comment_list': comment_list, 'c_form': c_form})
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        notice = Notice.objects.get(pk=nid)
        author = User.objects.get_by_natural_key(request.user.username)
        if c_form.is_valid():
            subject = c_form.cleaned_data['subject']
            author = author
            content = c_form.cleaned_data['content']
            belong_to = notice
            comment = Comment.objects.create(subject=subject, author=author, content=content, belong_to=belong_to)
            comment.save()
            return redirect('/n/notice/'+nid+'/')
        else:
            c_form = CommentForm()
            notice = Notice.objects.get(pk=nid)
            comment_list = Comment.objects.filter(belong_to=notice)
            return render(request, 'notice/notice_detail.html',
                          {'notice': notice, 'comment_list': comment_list, 'c_form': c_form})

@login_required
def create_bulletin(request):
    if request.method == 'GET':
        b_form = BulletinForm()
        return render(request, 'notice/create_bulletin.html', {'b_form': b_form})
    if request.method == 'POST':
        b_form = BulletinForm(request.POST)
        user = User.objects.get_by_natural_key(request.POST.get('creator'))
        if b_form.is_valid():
            name = b_form.cleaned_data['name']
            description = b_form.cleaned_data['description']
            bulletin = Bulletin.objects.create(name=name, description=description, creator=user)
            bulletin.save()
            return render(request, 'notice/info.html', {'msg': 'Bulletin Created!'})
        else:
            b_form = BulletinForm()
            return render(request, 'notice/create_bulletin.html', {'b_form': b_form})

@login_required
def post_notice(request, bid):
    if request.method == 'GET':
        n_form = NoticeForm()
        return render(request, 'notice/post_notice.html', {'n_form': n_form, 'bid': bid})
    if request.method == 'POST':
        n_form = NoticeForm(request.POST)
        user = User.objects.get_by_natural_key(request.POST.get('author'))
        bulletin = Bulletin.objects.get(pk=bid)
        if n_form.is_valid():
            title = n_form.cleaned_data['title']
            content = n_form.cleaned_data['content']
            notice = Notice.objects.create(title=title, author=user, bulletin=bulletin, content=content)
            notice.save()
            return render(request, 'notice/info.html', {'msg': 'Notice Posted!'})
        else:
            n_form = NoticeForm()
            return render(request, 'notice/post_notice.html', {'n_form': n_form})

@login_required
def my_bulletin(request):
    user = User.objects.get_by_natural_key(request.user.username)
    created_bulletins = Bulletin.objects.filter(creator=user)
    followed_bulletins = Bulletin.objects.filter(follower=user)
    return render(request, 'notice/my_bulletins.html', {'created_bulletins': created_bulletins,
                                                         'followed_bulletins': followed_bulletins})

@login_required
def search_bulletin(request):
    if request.method == 'GET':
        return render(request, 'notice/search_result.html')
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        bulletin_list = Bulletin.objects.filter(name__contains=keyword)
        return render(request, 'notice/search_result.html', {'bulletin_list': bulletin_list})

@login_required
def follow_bulletin(request, bid):
    bulletin = Bulletin.objects.get(pk=bid)
    user = User.objects.get_by_natural_key(request.user.username)
    bulletin.follower.add(user)
    return redirect('/n/browse_bulletins/')

@login_required
def unfollow_bulletin(request, bid):
    bulletin = Bulletin.objects.get(pk=bid)
    user = User.objects.get_by_natural_key(request.user.username)
    bulletin.follower.remove(user)
    bulletin.save()
    return redirect('/n/browse_bulletins/')

@login_required
def delete_bulletin(request, bid):
    user = User.objects.get_by_natural_key(request.user.username)
    bulletin = Bulletin.objects.get(pk=bid)
    if bulletin.creator == user:
        bulletin.delete()
        return redirect('/n/browse_bulletins/')
    else:
        return render(request, 'notice/info.html', {'msg': 'Invalid Request'})


@login_required
def delete_notice(request, nid):
    user = User.objects.get_by_natural_key(request.user.username)
    notice = Notice.objects.get(pk=nid)
    if notice.author == user:
        bid = notice.bulletin.pk
        notice.delete()
        return redirect('/n/browse_notices/'+ str(bid) +'/')
    else:
        return render(request, 'notice/info.html', {'msg': 'Invalid Request'})

@login_required
def remove_comment(request, cid):
    user = User.objects.get_by_natural_key(request.user.username)
    comment = Comment.objects.get(pk=cid)
    if comment.author == user:
        nid = comment.belong_to.pk
        comment.delete()
        return redirect('/n/notice/'+ str(nid) +'/')
    else:
        return render(request, 'notice/info.html', {'msg': 'Invalid Request'})





