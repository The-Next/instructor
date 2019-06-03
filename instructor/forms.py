from django import forms
from django.contrib import auth
from django.contrib.auth.models import User

class LoginForm(forms.Form):           #lable=''
    username = forms.CharField(widget=forms.TextInput(
                                    attrs={'class':'form-control', 'placeholder':'用户名'}))
    password = forms.CharField(widget=forms.PasswordInput(
                                    attrs={'class':'form-control', 'placeholder':'密码'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


class RegForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=6, widget=forms.TextInput(
                                    attrs={'class':'form-control', 'placeholder':'请输入6-20位用户名'}))
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(
                                    attrs={'class':'form-control', 'placeholder':'请输入Email地址'}))
    password = forms.CharField(min_length=6, widget=forms.PasswordInput(
                                    attrs={'class':'form-control', 'placeholder':'请输入密码'}))
    password_again = forms.CharField(min_length=6, widget=forms.PasswordInput(
                                    attrs={'class':'form-control', 'placeholder':'再输入一次密码'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('该邮箱已被注册')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次输入的密码不一致')
        return password_again