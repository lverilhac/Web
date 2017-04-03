from django import forms


class RegisterForm(forms.Form):
    login = forms.CharField(max_length=10)
    passwd = forms.CharField(max_length=10)

