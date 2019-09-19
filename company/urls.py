from django.urls import path

from . import views



urlpatterns = [
    # path('GetImage', views.GetImage.as_view() , name='GetImage'),

    path('AdList', views.AdList.as_view() , name='AdList'),

]
