from django.urls import path, include
from .views import homepage, flightpage

urlpatterns = [
    path('', homepage.as_view(), name='home'),
    path('flight/', flightpage.as_view(), name='flight'),
]