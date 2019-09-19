from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny , IsAuthenticated
from itertools import chain
from rest_framework.response import Response
from rest_framework import status




from .models import *
from .serializers import *
# Create your views here.




class AdList(APIView):

    serializer_class = AdSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # queryset = list(chain(Company.objects.filter(status='ad') , Company.objects.filter(status='on_demand'))).
        li = []
        for ins in Company.objects.order_by('-id'):
            if ins.status == 'ad' or ins.status == 'on_demand':
                li.append(AdSerializer(ins).data)
        return Response(li, status=status.HTTP_200_OK)
