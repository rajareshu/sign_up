from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('Login/',views.Login),
    path('ragistration/',views.ragistration),
    path('Login_data/',views.Login_page),
    
    path('table/',views.table)
]