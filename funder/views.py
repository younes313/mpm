from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .serializers import *
from . models import *
from company.models import *
# Create your views here.



class FunderLogin(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        try:
            user = User.objects.get(username=request.data['phone_number'])
            if not user.check_password(request.data['national_code']):
                return Response({'status': False, 'error': '104'}, status=status.HTTP_200_OK)   #incorrect user pass
            else:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'status':True, 'token': token.key}, status=status.HTTP_200_OK)
        except:
            return Response({'status': False, 'error': '104'}, status=status.HTTP_200_OK)   #incorrect user pass


class FunderSignUp(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = FunderSignUpSerializer(data = request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(username=serializer.data['phone_number'], password=serializer.data['national_code'],
                                                email=serializer.data['email'], first_name=serializer.data['first_name'], last_name=serializer.data['last_name'],
                                                )
                funder = Funder.objects.create(user=user, phone_number=serializer.data['phone_number'], national_code= serializer.data['national_code'])
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'status':True, 'token': token.key}, status=status.HTTP_200_OK)
            except:
                return Response({'status':False , 'error':'103'}, status=status.HTTP_200_OK) # inapropriate input


class GetUserInfo(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        funder = Funder.objects.get(user=request.user)
        serializer = GetUserInfoSerializer( funder)

        return Response(serializer.data, status= status.HTTP_200_OK)



class GetHistory(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        funder = Funder.objects.get(user = request.user)
        dic = dict()

        serializer = GetHistorySerialzer(History.objects.filter(funder=funder, public_or_specefic = 'عام', help_or_contribute='کمک' ), many=True)
        dic['public_help'] = serializer.data

        serializer = GetHistorySerialzer(History.objects.filter(funder = funder, public_or_specefic = "عام", help_or_contribute="سهام" ), many=True)
        dic['public_stock'] = serializer.data

        serializer = GetHistorySerialzer(History.objects.filter(funder = funder, public_or_specefic = "خاص", help_or_contribute="کمک" ), many=True)
        dic['specefic_help'] = serializer.data

        serializer = GetHistorySerialzer(History.objects.filter(funder = funder, public_or_specefic = "خاص", help_or_contribute="سهام" ), many=True)
        dic['specefic_stock'] = serializer.data

        return Response(dic, status=status.HTTP_200_OK)



class Funding(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        serializer = FundingSerializer(data=request.data)
        if serializer.is_valid():
            funder = Funder.objects.get(user=request.user)
            if serializer.data['company_id'] == 0:
                history = History(company=None, funder=funder, money = serializer.data['money'], public_or_specefic=serializer.data['public_or_specefic'], help_or_contribute=serializer.data['help_or_contribute'] )
                funder.total_help += history.money
                funder.save()
            else:
                company = Company.objects.get(id=serializer.data['company_id'])
                if serializer.data['money'] > (0.05*company.needed_fee) :
                    return Response({'status':False, 'error':'101'}, status=status.HTTP_200_OK) # more than 5%
                if serializer.data['money'] < 20000 :
                    return Response({'status':False, 'error':'102'}, status=status.HTTP_200_OK) # less than 20000
                history = History(company=company, funder=funder, money= serializer.data['money'], public_or_specefic=serializer.data['public_or_specefic'], help_or_contribute=serializer.data['help_or_contribute'] )

                funder.total_investment += history.money
                funder.save()

                company.remained_fee -= serializer.data['money']
                company.fee_count += 1
                if company.remained_fee == 0 :
                    company.status = 'call'
                company.save()
            history.save()



            return Response({'status':True}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)
