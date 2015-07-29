#-*- coding: utf-8 -*-

import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'form-control input-lg'}),max_length=30)
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email', 'class':'form-control input-lg'}))
    password1 = forms.CharField(
        label = '',
        widget = forms.PasswordInput(attrs = {'placeholder': 'Password', 'class':'form-control input-lg'})
    )
    password2 = forms.CharField(
        label = '',
        widget = forms.PasswordInput(attrs = {'placeholder': 'Password again', 'class':'form-control input-lg'})
    )

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2

        raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError(
                '사용자 이름은 알파벳, 숫자, 밑줄(_)만 가능합니다.'
            )
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('이미 사용 중인 사용자 이름입니다.')


