from django import forms
from django.contrib.auth.models import User
from .models import Profile


class CreatUserForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password reset', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        cd = CreatUserForm.clean(self)
        p = cd.get('password')
        p2 = cd.get('password2')
        if p != p2:
            raise forms.ValidationError('password not match')


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileEditForm(forms.ModelForm):
    DOB = forms.DateField(label='DOB(DD/MM/YYYY)',widget=forms.DateInput(format='%d/%m/%Y'), required=False)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'DOB', 'mobile_no', 'address']









