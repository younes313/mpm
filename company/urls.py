from django.urls import path

from . import views



urlpatterns = [
    # path('GetImage', views.GetImage.as_view() , name='GetImage'),

    path('GetCompanyById', views.GetCompanyById.as_view() , name='GetCompanyById'),
    path('GetOnDemandCompany', views.GetOnDemandCompany.as_view() , name='GetOnDemandCompany'),
    path('AdList', views.AdList.as_view() , name='AdList'),

]
