from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from user.models import consultancy_service,dogs_advert,birds_advert,cart,Order
from administrator.models import pets_sale,petscategory,breeds
from administrator.forms import sales
from django.contrib import messages
from .forms import dog,bird,vetnary,boarder,transport,grooming,walking,training,advert_vetnary
from django.contrib.auth import get_user_model
from Dreamgarden.settings import EMAIL_HOST_USER

from django.core.mail import send_mail
User = get_user_model()



# Create your views here.
def view_pets(request):
    if request.method == 'GET': 
        result=pets_sale.objects.filter(product_type='pet')
        return render(request,'view_pets.html',{"pets":result})

def view_accessories(request):
    if request.method == 'GET': 
        result=pets_sale.objects.filter(product_type='Accessories')
        return render(request,'view_accessories.html',{"pets":result})

def pet_details(request,id):
    result=get_object_or_404(pets_sale,id=id)
    return render(request,'pet_details.html',{"pets":result})


def boarder_service(request):
    form = boarder(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            answer = form.save(commit=False)
            answer.service_type=request.POST['service_type']
            answer.customer_id=request.user.id
            answer.save()
            return redirect('/')

    return render(request,'boarder_service.html')

def vetnary_service(request):
    form = vetnary(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            answer = form.save(commit=False)
            answer.service_type=request.POST['service_type']
            answer.customer_id=request.user.id
            answer.save()
            return redirect('/')

    return render(request,'vetnary_service.html')

def transport_service(request):
    form = transport(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            answer = form.save(commit=False)
            answer.service_type=request.POST['service_type']
            answer.customer_id=request.user.id
            answer.save()
            return redirect('/')

    return render(request,'transport_service.html')

def walker_service(request):
    form = walking(request.POST)
    if request.method=='POST':
        if form.is_valid():
            answer = form.save(commit=False)
            answer.service_type=request.POST['service_type']
            answer.customer_id=request.user.id
            answer.save()
            return redirect('/')
    return render(request,'walker_service.html')

def grooming_service(request):
    form = grooming(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            answer = form.save(commit=False)
            answer.service_type=request.POST['service_type']
            answer.customer_id=request.user.id
            answer.save()
            return redirect('/')
    return render(request,'grooming_service.html')

def trainer_service(request):
    form = training(request.POST)
    if request.method=='POST':
        if form.is_valid():
            answer = form.save(commit=False)
            answer.service_type=request.POST['service_type']
            answer.customer_id=request.user.id
            answer.save()
            return redirect('/')
    return render(request,'trainer_service.html')


def boarder_advert(request):
    return render(request,'boarder_advert.html')

def grooming_advert(request):
    return render(request,'grooming_advert.html')

def trainer_advert(request):
    return render(request,'trainer_advert.html')

def transport_advert(request):
    return render(request,'transport_advert.html')

def walker_advert(request):
    return render(request,'walker_advert.html')

def vetnary_advert(request):
    form = advert_vetnary(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            answer = form.save(commit=False)
            answer.advert_type=request.POST['advert_type']         
            answer.save()
            messages.success(request, 'Enrolled Succesful')
            return redirect('/')

    return render(request,'vetnary_advert.html')

@login_required(login_url='administrator:login')
def dog_advert(request):
    
    if request.method=='POST':
        form = dog(request.POST,request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.customer_id=request.user.id
            answer.save()
            return redirect('/')
    else:
        form=dog()

    return render(request,'dogs_advert.html',{'form':form})

@login_required(login_url='administrator:login')
def consultancy(request):
    user=request.user
    if request.method=='POST':
        email=request.POST['email']
        pet=request.POST['pet']
        breed=request.POST['breed']
        advice=request.POST['advice']
        consultancy=consultancy_service(email=email,pet=pet,breed=breed,advice=advice)
        consultancy.save()
        return redirect('/')
    return render(request,'consultancy_form.html',{'user':user})

@login_required(login_url='administrator:login')
def birds_advert(request):
   
    if request.method=='POST':
        form = bird(request.POST,request.FILES)
        if form.is_valid():

            answer = form.save(commit=False)
            answer.customer_id=request.user.id
            answer.save()
            return redirect('/')
    else:
        form=bird()       
         
    return render(request,'birds_advert.html',{'form':form})

def delete_pet(request,id):
    pet=pets_sale.objects.get(id=id)
    pet.delete()
    return render(request,'index.html')

def edit_pets(request, id):
    results=petscategory.objects.all
    results1=breeds.objects.all
    server = get_object_or_404(pets_sale, pk=id)
    form = sales(data=request.POST, files=request.FILES, instance=server)
    if form.is_valid():
        edit=form.save(commit=False)
        edit.save()
        messages.success(request,"Updated Successfully")
        return redirect('/')
    return render(request, 'editpets.html', {'pets':server,"showpets":results,"showbreeds":results1})

@login_required(login_url='administrator:login')
def add_to_cart(request):
    context={}
    items = cart.objects.filter(user__id=request.user.id,status=False)
    context["items"] = items

    if request.user.is_authenticated:
        if request.method=="POST":
            pid = request.POST["pid"]
            qty = request.POST["qty"]
            is_exist = cart.objects.filter(product__id=pid,user__id=request.user.id,status=False)
            if len(is_exist)>0:
                context["msz"] = "Item Already Exists in Your Cart"
                context["cls"] = "alert alert-warning"
            else:    
                product =get_object_or_404(pets_sale,id=pid)
                usr = get_object_or_404(User,id=request.user.id)
                c = cart(user=usr,product=product,quantity=qty)
                c.save()
                context["msz"] = "{} Added in Your Cart".format(product.id)
                context["cls"] = "alert alert-success"
    else:
        context["status"] = "Please Login First to View Your Cart"
    return render(request,"cart_detail.html",context)

@login_required(login_url='administrator:login')
def get_cart_data(request):
    items = cart.objects.filter(user__id=request.user.id, status=False)
    sale,total,quantity =0,0,0
    for i in items:
       
        total += float(i.product.price)*i.quantity
        quantity+= int(i.quantity)

    res = {
        "total":total,"offer":sale,"quan":quantity,
    }
    return JsonResponse(res)

def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity)

    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cart_obj = get_object_or_404(cart,id=id)
        cart_obj.delete()
        return HttpResponse(1)

@login_required(login_url='administrator:login')
def buy_now(request):
    if request.method == 'POST':
        
        product_ids=request.POST['product_ids']
        total_amount=request.POST['total_amount']
        usr = User.objects.get(username=request.user.username)
        ord = Order(cust_id=usr,product_ids=product_ids,total_amount=total_amount)
        ord.save()
        messages.success(request,"Order Placed Successfully")
    return redirect('/')


@login_required(login_url='administrator:login')
def order(request):
    items = cart.objects.filter(user_id__id=request.user.id,status=False)
    products=""
    amt=0
    inv = "INV10001-"
    cart_ids = ""
    p_ids =""
    
    for j in items:
        products += str(j.product.id)+"\n"
        p_ids += str(j.product.id)+","
        amt += float(j.product.price)*(j.quantity)
        inv +=  str(j.id)
        cart_ids += str(j.id)+","

    usr = User.objects.get(username=request.user.username)
    ord = Order(cust_id=usr,cart_ids=cart_ids,product_ids=p_ids,total_amount=amt)
    ord.save()
    ord.invoice_id = str(ord.id)+inv

    ord.save()
    request.session["order_id"] = ord.id
    messages.success(request,"Your Order Has been Placed")


    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()
        
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return redirect('/')
    
@login_required(login_url='administrator:login')
def order_history(request):
    context = {}
    all_orders = []
    orders = Order.objects.filter(cust_id__id=request.user.id).order_by("-id")
    for order in orders:
        products = []
        for id in order.product_ids.split(",")[:-1]:
            pro = pets_sale.objects.get(id=id)
            products.append(pro)
            print(pro)
        ord = {
            "order_id":order.id,
            "products":products,
            "invoice":order.invoice_id,
            "status":order.status,
            "date":order.processed_on,
        }
        all_orders.append(ord)
    context["order_history"] = all_orders
    return render(request,"order_history.html",context)

def buynow(request,id):
    pet=pets_sale.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        pet=request.POST['pet']
        num=request.POST['num']
        no=request.POST['no']
        street=request.POST['street']
        area=request.POST['area']
        city=request.POST['city']
        country=request.POST['country']
        pin=request.POST['pin']
        msg="Name:"+name + "Email:"+email +"Mobile :"+num+ "Pet :"+pet +"Address :"+no +street +area +city +country +pin
        send_mail('Order',msg,EMAIL_HOST_USER, ['janakiraman0619@gmail.com'], fail_silently = False)
        messages.success(request,"Your request has been recorded!!We will Reach out to You shortly")
        return redirect('/')
    return render(request,"buy.html",{'i':pet})