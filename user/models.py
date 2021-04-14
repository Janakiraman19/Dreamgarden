from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from administrator.models import pets_sale

User = get_user_model()

# Create your models here.
class service(models.Model):
      customer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      service_type=models.CharField(max_length=25)
      pet=models.CharField(max_length=20,null=True)
      breed=models.CharField(max_length=20)
      age=models.CharField(max_length=20)
      address=models.CharField(max_length=100,null=True)
      problem_description=models.CharField(max_length=150,null=True)
      medication_record=models.ImageField(max_length=100,null=True)
      diet_plan=models.CharField(max_length=20,null=True)
      boarding_days=models.CharField(max_length=20,null=True)
      basic_training=models.CharField(max_length=20,null=True)
      include_supplement=models.CharField(max_length=20,null=True)
      pickup_location=models.CharField(max_length=100,null=True)
      drop_location=models.CharField(max_length=20,null=True)
      transport_type=models.CharField(max_length=20,null=True)
      pet_verification=models.CharField(max_length=20,null=True)
      new_crate=models.CharField(max_length=20,null=True)
      current_pic=models.ImageField(max_length=100,null=True)
      grooming_description=models.CharField(max_length=100,null=True)
      reffered_pic=models.ImageField(max_length=20,null=True)
      timing=models.CharField(max_length=20,null=True)
      walker_training=models.CharField(max_length=20,null=True)
      training_type=models.CharField(max_length=20,null=True)
      other=models.CharField(max_length=20,null=True)

class birds_advert(models.Model):
     customer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     breed=models.CharField(max_length=20)
     Age=models.CharField(max_length=20)
     bird_type=models.CharField(max_length=20)
     pair_type=models.CharField(max_length=20)
     dna_test=models.CharField(max_length=20)
     ring=models.CharField(max_length=20)
     location=models.CharField(max_length=50)
     contact=models.IntegerField()
     image=models.ImageField(max_length=100)
     image1=models.ImageField(max_length=100)
     image2=models.ImageField(max_length=100)
     price=models.IntegerField()

class consultancy_service(models.Model):
     email=models.CharField(max_length=25)
     pet=models.CharField(max_length=20)
     breed=models.CharField(max_length=20)
     advice=models.CharField(max_length=200)

class dogs_advert(models.Model):
     customer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     breed=models.CharField(max_length=20)
     Age=models.CharField(max_length=20)
     sex=models.CharField(max_length=20)
     kci_certificate=models.CharField(max_length=20)
     location=models.CharField(max_length=50)
     contact_number=models.CharField(max_length=20)
     image=models.ImageField(max_length=100)
     image1=models.ImageField(max_length=100)
     image2=models.ImageField(max_length=100)
     price=models.CharField(max_length=30)

class cart(models.Model):
    user =models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(pets_sale,on_delete = models.CASCADE)
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    added_on =models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now=True,null=True)

class Order(models.Model):
    cust_id = models.ForeignKey(User,on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=250,null=True)
    product_ids = models.CharField(max_length=250)
    invoice_id = models.CharField(max_length=250,null=True)
    status = models.BooleanField(default=False,null=True)
    processed_on = models.DateTimeField(auto_now_add=True)
    total_amount=models.CharField(max_length=50,null=True)

class service_advert(models.Model):
     advert_type=models.CharField(max_length=30)
     name=models.CharField(max_length=25)
     email=models.CharField(max_length=25)
     contact=models.CharField(max_length=25)
     location=models.CharField(max_length=250)
     degree=models.CharField(max_length=25)
     specialist_for=models.CharField(max_length=25)
     door_step=models.CharField(max_length=25)
     certificate=models.ImageField(max_length=100)
     cage_size=models.CharField(max_length=25)
     diet_plan=models.CharField(max_length=25)
     bathing=models.CharField(max_length=25)
     vedio_time=models.CharField(max_length=25)
     walk_time=models.CharField(max_length=25)
     routes=models.CharField(max_length=250)
     vehicle=models.CharField(max_length=25)
     vehicle_number=models.CharField(max_length=25)
     vehicle_type=models.CharField(max_length=10)
     driving_lisence=models.ImageField(max_length=100)
     aadhar_card=models.ImageField(max_length=100)
     comfort=models.CharField(max_length=100)
     working_hours=models.CharField(max_length=25)
     pre_work=models.ImageField(max_length=100)
     timing=models.CharField(max_length=25)
     address_proof=models.CharField(max_length=25)
     boarding=models.CharField(max_length=25)
     pre_work=models.FileField(max_length=250)



   
     
     
