from django import forms

class Signup(forms.Form):
    username=forms.CharField(required=False)
    password=forms.PasswordInput()
   