from django import forms


class userform(forms.Form):
    username = forms.CharField(label='user')
    password = forms.CharField(label='pass')
