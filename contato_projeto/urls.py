from django.urls import path, include
from contato import views

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('contact/', include('contato.urls')),
]
