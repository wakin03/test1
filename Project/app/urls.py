from django.urls import path
    
from .views import HomePageView, AboutPageView, BasePageView, ContactPageView, ServicePageView

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', BasePageView.as_view(), name='base'),
     path('contact/', ContactPageView.as_view(), name='contact'),
     path('service/',ServicePageView.as_view(), name='service'),

]