from user import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


app_name="user"
urlpatterns=[
    path('boarder_service',views.boarder_service,name='boarder_service'),
    path('vetnary_service',views.vetnary_service,name='vetnary_service'),
    path('transport_service',views.transport_service,name='transport_service'),
    path('walker_service',views.walker_service,name='walker_service'),
    path('grooming_service',views.grooming_service,name='grooming_service'),
    path('trainer_service',views.trainer_service,name='trainer_service'),
    path('view_pets',views.view_pets,name='view_pets'),
    path('view_accessories',views.view_accessories,name='view_accessories'),
    path('<int:id>',views.pet_details,name='pet_details'),
    path('delete_pet/<int:id>',views.delete_pet,name='delete_pet'),
    path('editpets/<int:id>',views.edit_pets,name='edit_pets'),
  

     path('dog_advert',views.dog_advert,name='dog_advert'),
      path('birds_advert',views.birds_advert,name='birds_advert'),
     path('consultancy',views.consultancy,name='consultancy'),
     
      path("buy_now",views.buy_now,name="buy_now"),
     path("cart",views.add_to_cart,name="cart"),
    path("get_cart_data",views.get_cart_data,name="get_cart_data"),
    path("change_quan",views.change_quan,name="change_quan"),
    path('order',views.order,name='order'),
    path('order_history',views.order_history,name='order_history'),
    path('<int:id>/buynow',views.buynow,name="buynow"),



     path('boarder_advert',views.boarder_advert,name='boarder_advert'),
    path('vetnary_advert',views.vetnary_advert,name='vetnary_advert'),
    path('transport_advert',views.transport_advert,name='transport_advert'),
    path('walker_advert',views.walker_advert,name='walker_advert'),
    path('grooming_advert',views.grooming_advert,name='grooming_advert'),
    path('trainer_advert',views.trainer_advert,name='trainer_advert'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)