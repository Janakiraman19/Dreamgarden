from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from .forms import sales,ProfileEditForm,asales
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from administrator.models import petscategory,breeds,pets_sale
from user.models import consultancy_service,dogs_advert,birds_advert,service,Order
from django.core.mail import send_mail
from Dreamgarden.settings import EMAIL_HOST_USER
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.          
def login(request):
    if request.method== 'POST':
        email=request.POST['email']
        password=request.POST['password']
        
        if User.objects.filter(email=email).exists():
            username = User.objects.get(email=email.lower()).username
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,"Welcome")
                return redirect("/")
            else:
                print("invalid")
                messages.info(request, 'Invalid Login Details')
                return render(request,"login.html")
        else:
            messages.info(request,"Invalid E mail")
    return render(request,'login.html')   
   

def addpets(request):
    results=petscategory.objects.all
    results1=breeds.objects.all
    
    if request.method=='POST':
        form = sales(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.product_type=request.POST['product_type']
            answer.save()
            return redirect('/')
    else:
        form=sales()
    return render(request, "addpets.html",{"showpets":results,"showbreeds":results1})

def addaccessories(request):
    results=petscategory.objects.all
    
    if request.method=='POST':
        form = asales(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.product_type=request.POST['product_type']
            answer.save()
            return redirect('/')
    else:
        form=asales()
    return render(request,'addaccessories.html',{"showpets":results})

def consultancy_response(request,id):
    result=get_object_or_404(consultancy_service,id=id)
    return render(request,'consultancy_response.html',{'email':result})

def consultancy_request(request):
    result=consultancy_service.objects.all
    return render(request,'consultancy_request.html',{"request":result})
    
def service_response(request,id):
    result=get_object_or_404(service,id=id)
    return render(request,'service_response.html',{'email':result})

def service_mail(request,id):
    if request.method=='POST':
        to=request.POST['to']
        reply=request.POST['reply']
        send_mail('hi',reply, EMAIL_HOST_USER, [to], fail_silently = False)
   
   
    return redirect("/")


def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Id Taken")
            else:
                user=User.objects.create_user(first_name=name,username=email,email=email,last_name=contact,password=password1)
                user.save()
                messages.success(request,"Registered Successfully")
                return redirect("/")
        else:
            messages.info(request,"Password Mismatch")
        return render(request,"register.html")

    else:
        
        return render(request,'register.html')
def addpetsname(request):
    if request.method =='POST':
        petsname=request.POST['pet']
        pets=petscategory(petname=petsname)
        pets.save()
        messages.success(request, 'Pet Added Successfully')
        return render(request,'addpets.html')

def addbreedsname(request):
    results=petscategory.objects.all()
    if request.method =='POST':
        petsname=request.POST['petsname']
        breedname=request.POST['breedname']
        breed=breeds(petname=petsname,breedname=breedname)
        breed.save()
        messages.success(request, 'Breed Added Successfully')
    return render(request, "addpets.html",{"showpets":results})

def consultancy_mail(request,id):
    if request.method=='POST':
        to=request.POST['to']
        advice=request.POST['advice']
        reply=request.POST['reply']
        send_mail(advice,reply, EMAIL_HOST_USER, [to], fail_silently = False)
        instance = consultancy_service.objects.get(id=id)
        instance.delete()
    result=consultancy_service.objects.all
    return render(request,'consultancy_request.html',{"request":result})



@login_required(login_url='administrator:login')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(data=request.POST,instance=request.user)        
        email=request.POST['email']
        if form.is_valid():
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Id Taken")
            else:
                form.save()
                messages.success(request,"Updated Successfully")
                return redirect('/')
    else:
        form=ProfileEditForm(instance=request.user)
    return render(request,'edit_profile.html',{'form':form})

@login_required(login_url='administrator:login')
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('change_password')
		else:
			messages.error(request, 'Please correct the error below.')

	else:
		form = PasswordChangeForm(user=request.user)

	return render(request, 'change_password.html', {'form':form})

def viewsales_advert(request):
    result=dogs_advert.objects.all
    result1=birds_advert.objects.all
    return render(request,'viewsales_advert.html',{'result':result,'result1':result1})

def view_service(request):
    vetnary=service.objects.filter(service_type='Vetnary')
    boarder=service.objects.filter(service_type='Boarder')
    transport=service.objects.filter(service_type='Transport')
    grooming=service.objects.filter(service_type='Grooming')
    walker=service.objects.filter(service_type='Walker')
    trainer=service.objects.filter(service_type='Dog_trainer')
    return render(request,'view_service.html',{'vetnary':vetnary,'boarder':boarder,'transport':transport,'walker':walker,'trainer':trainer,'grooming':grooming})


def delete_dog(request,id):
    pet=dogs_advert.objects.get(id=id)
    pet.delete()
    return render(request,'index.html')

def delete_bird(request,id):
    pet=birds_advert.objects.get(id=id)
    pet.delete()
    return render(request,'index.html')

def delete_service(request,id):
    pet=service.objects.get(id=id)
    pet.delete()
    return render(request,'index.html')

@login_required(login_url='administrator:login')
def all_orders(request):
    context = {}
  
    all_orders = []
    orders = Order.objects.all()
    for order in orders:
        products = []
        for id in order.product_ids.split(",")[:-1]:
            pro = get_object_or_404(pets_sale, id=id)
            products.append(pro)
            print(pro)
           
        ord = {
            "order_id":order.id,
            "products":products,
            "invoice":order.invoice_id,
            "status":order.status,
            "date":order.processed_on,
            "total_amount":order.total_amount,
            "cust_id":order.cust_id,
        }
        all_orders.append(ord)
    context["order_history"] = all_orders
    return render(request,"orders.html",context)
