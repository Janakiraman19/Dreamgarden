from django.forms import ModelForm
from django import forms
from .models import consultancy_service,dogs_advert,birds_advert,service,service_advert


Choice = [("Available","Available"),("Not-Available","Not-Available")]
sex=[("Male","Male"),("Female","Female")]
bird_type=[("Tamed","Tamed"),("Wild","Wild")]
pair_type=[("Single","Single"),("Pair","Pair"),("Settled Pair","Settled Pair")]
class consultancy(ModelForm):
    class Meta:
        model=consultancy_service
        fields='__all__'

class dog(ModelForm):
     sex=forms.CharField(widget=forms.Select(choices=sex))
     kci_certificate= forms.CharField( widget=forms.RadioSelect(choices=Choice))
     class Meta:

        model=dogs_advert
        fields=['breed','Age','sex','kci_certificate','location','contact_number','image','image1','image2','price']
    
class bird(ModelForm):
    bird_type=forms.CharField(widget=forms.Select(choices=bird_type))
    pair_type=forms.CharField(widget=forms.RadioSelect(choices=pair_type))
    dna_test=forms.CharField( widget=forms.RadioSelect(choices=Choice))
    ring=forms.CharField( widget=forms.RadioSelect(choices=Choice))
    class Meta:
        model=birds_advert
        exclude = ('customer',)


class vetnary(ModelForm):
    class Meta:
        model=service
        fields=['pet','breed','age','problem_description','address','medication_record']

class boarder(ModelForm):
    class Meta:
        model=service
        fields=['pet','breed','age','address','diet_plan','boarding_days','basic_training','include_supplement']

class transport(ModelForm):
    class Meta:
        model=service
        fields=['pet','breed','age','pickup_location','drop_location','transport_type','pet_verification','new_crate']

class grooming(ModelForm):
    class Meta:
        model=service
        fields=['breed','age','address','current_pic','grooming_description','reffered_pic']

class walking(ModelForm):
    class Meta:
        model=service
        fields=['breed','age','timing','address','walker_training']

class training(ModelForm):
    class Meta:
        model=service
        fields=['breed','age','address','training_type','other']

class advert_vetnary(ModelForm):
    class Meta:
        model=service_advert
        fields=['name','email','contact','location','degree','specialist_for','door_step','certificate']