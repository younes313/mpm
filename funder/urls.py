from django.urls import path

from . import views



urlpatterns = [
    # path('GetImage', views.GetImage.as_view() , name='GetImage'),

    path('Funding', views.Funding.as_view() , name='Funding'),

]
