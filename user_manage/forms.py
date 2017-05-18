from django import forms

class LoginForm(forms.Form):
    uid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RegisterForm(forms.Form):
    uid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'onblur': 'authentication()'}),
                          required=True,
                          min_length=6,
                          max_length=20,
                          error_messages={'required': 'at least 6 characters including letters, digits and underscores'})
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                            required=True, error_messages={'required': 'this field cannot be empty'})
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                          required=True,
                          min_length=6,
                          max_length=20,
                          error_messages={'required': 'at least 6 characters including letters, digits and symbols'})
    re_pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Password'}))
    sec_q = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Security Question'}),
                            required=True,
                            error_messages={'required': 'this field cannot be empty'})
    sec_a = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Answer'}),
                            required=True,
                            error_messages={'required': 'this field cannot be empty'})

class FindPasswordForm(forms.Form):
    sec_a = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Answer'}))

class ModifyPasswordForm(forms.Form):
    old_pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old Password'}))
    new_pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    re_pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Password'}))

class ResetPasswordForm(forms.Form):
    new_pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    re_pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Password'}))