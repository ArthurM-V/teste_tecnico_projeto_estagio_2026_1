from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Mensagem

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ["nome", "email", "mensagem"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full  border-b px-3 py-2",
            "placeholder": "Usuário"
        })
    )

    password = forms.CharField(
        label = "Senha",
        widget=forms.PasswordInput(attrs={
            "class": "w-full  border-b px-3 py-2",
            "placeholder": "Senha"
        })
    )