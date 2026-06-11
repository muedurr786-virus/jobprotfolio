from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserModelForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username','email','password1','password2']

class Authform(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username','password1']


class UpdatedProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        exclude = ['user', 'bmr']

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItemModel
        fields = ['item_name', 'calory']
