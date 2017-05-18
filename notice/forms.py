from django import forms

class BulletinForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of Bulletin'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description'}))

class NoticeForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Content'}))

class CommentForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Content'}))