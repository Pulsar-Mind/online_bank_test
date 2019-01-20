from django.contrib import admin
from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.login,{'template_name': 'accounts/landingpage.html'}, name='login'),	#auth_views function provided by django, Wurzel Pfad
    path('logout', auth_views.logout,{'next_page': '/'}, name='logout'),	
    path('checkiban/<iban>', views.checkiban),
    path('accounts/profile/', views.myprofile),
    path('accounts/<iban>', views.myaccount),
    path('transaction', views.transaction),
    path('alltransactions', views.alltransactions),
    path('iban_api_sender/<iban>', views.checkiban_sender_api),
    path('iban_api_receiver/<iban>', views.checkiban_receiver_api),
    path('amount_api/<iban>/<amount>', views.checkamount_sender_api),

]


