from django import forms

class UserRegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
        'id': 'inputEmail4'
    }))

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create Password'}))

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
        'id': 'inputEmail4'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Create Password', 
        'class': 'form-control',
        'id': 'inputpassword4'
    }))