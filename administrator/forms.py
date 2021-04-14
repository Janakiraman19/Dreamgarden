from django.forms import ModelForm
from django import forms
from .models import pets_sale
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


# define the class of a form
# model=login
#username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
 #email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  #password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
   # password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class sales(ModelForm):
   class Meta:
       model = pets_sale
       fields=['petname','breedname','age','quantity','product_description','image','image1','image2','price','sex','rating']

class asales(ModelForm):
   class Meta:
       model = pets_sale
       fields=['petname','name','quantity','product_description','image','image1','image2','price']
    
class ProfileEditForm(UserChangeForm):
    class Meta:
        model = User

        fields = ('first_name','email','last_name')


