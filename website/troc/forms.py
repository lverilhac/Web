from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",max_length=30)
    adresse_mail = forms.CharField(label="Adresse mail",max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)

