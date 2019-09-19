from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.core.mail import EmailMessage
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect


from .serializers import *
from . models import *
from company.models import *
# Create your views here.




@permission_classes((IsAuthenticated,))
class Funding(APIView):

    def post(self, request, format=None):
        serializer = FundingSerializer(data=request.data)
        if serializer.is_valid():
            company = Company.objects.get(id=serializer.data['company_id'])
            funder = Funder.objects.get(user=request.user)

            if serializer.data['money'] > (0.05*company.needed_fee) :
                return Response({'status':False, 'error':'101'}, status=status.HTTP_200_OK) # more than 5%
            if serializer.data['money'] < 20000 :
                return Response({'status':False, 'error':'102'}, status=status.HTTP_200_OK) # less than 20000


            history = History(company=company, funder=funder, money= serializer.data['money'], public_or_specefic=serializer.data['public_or_specefic'], help_or_contribute=serializer.data['help_or_contribute'] )
            history.save()

            company.remained_fee -= serializer.data['money']
            if company.remained_fee == 0 :
                company.status = 'call'
            company.save()


            return Response({'status':True}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)
