from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_us, name='about'),
    path('shorten/', views.Shorten.as_view(), name='shorten')
]

