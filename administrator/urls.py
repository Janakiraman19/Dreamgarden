from administrator import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name="administrator"
urlpatterns = [

path('login/',views.login, name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('password-request-link/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),

path('addpets/', views.addpets, name='addpets'),
path('addaccessories/', views.addaccessories, name='addaccessories'),
path('register/',views.register,name='register'),
path('addpets/addpetsname',views.addpetsname,name='addpetsname'),
path('addpets/addbreedsname',views.addbreedsname,name='addbreedsname'),
path('consultancy_request',views.consultancy_request,name='consultancy_request'),
path('consultancy_mail/<int:id>',views.consultancy_mail,name='consultancy_mail'),
path('<int:id>',views.consultancy_response,name='consultancy_response'),
path('service_response/<int:id>',views.service_response,name='service_response'),
path('service_response/service_mail/<int:id>',views.service_mail,name='service_mail'),
path('edit_profile',views.edit_profile,name='edit_profile'),
path('change_password',views.change_password,name='change_password'),
path('viewsales_advert',views.viewsales_advert,name='viewsales_advert'),
path('view_service',views.view_service,name='view_service'),
path('delete_service/<int:id>',views.delete_service,name='delete_service'),
path('delete_dog/<int:id>',views.delete_dog,name='delete_dog'),
path('delete_bird/<int:id>',views.delete_bird,name='delete_bird'),
path('all_orders',views.all_orders,name='all_orders'),



]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)