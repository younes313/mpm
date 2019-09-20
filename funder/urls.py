from django.urls import path

from . import views



urlpatterns = [
    # path('GetImage', views.GetImage.as_view() , name='GetImage'),

    path('FunderLogin', views.FunderLogin.as_view() , name='FunderLogin'),
    path('FunderSignUp', views.FunderSignUp.as_view() , name='FunderSignUp'),
    path('GetUserInfo', views.GetUserInfo.as_view() , name='GetUserInfo'),
    path('GetHistory', views.GetHistory.as_view() , name='GetHistory'),
    path('Funding', views.Funding.as_view() , name='Funding'),

]
