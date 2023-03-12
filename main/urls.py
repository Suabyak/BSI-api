from django.urls import path
from . import views


urlpatterns = [
    path('cipher_file/', views.cipher_file),
    path('decipher_file/', views.decipher_file)
]
