from django.db import models
from django.forms import ModelForm

class register(models.Model):
     name=models.CharField(max_length=67)
     email=models.EmailField(max_length=67)
     password=models.CharField(max_length=67)
     c_password=models.CharField(max_length=67)

class petscategory(models.Model):
    petname=models.CharField(max_length=60)

class breeds(models.Model):
    petname=models.CharField(max_length=100)
    breedname=models.CharField(max_length=67)

class pets_sale(models.Model):
    product_type=models.CharField(max_length=20)
    petname=models.CharField(max_length=100,null=True)
    breedname=models.CharField(max_length=30,null=True)
    name=models.CharField(max_length=21,null=True)
    age=models.CharField(max_length=20,null=True)
    product_description=models.CharField(max_length=70)
    quantity=models.CharField(max_length=20)
    image=models.ImageField(max_length=100)
    image1=models.ImageField(max_length=100)
    image2=models.ImageField(max_length=100)
    image3=models.ImageField(max_length=100)
    price=models.CharField(max_length=100)
    rating=models.CharField(max_length=10)
    sex=models.CharField(max_length=10)