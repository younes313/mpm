from rest_framework.generics import ListAPIView ,CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny , IsAuthenticated
from itertools import chain
from rest_framework.response import Response
from rest_framework import status


from .models import *
from .serializers import *
# Create your views here.


class GetCompanyById(APIView):
    permission_classes = (IsAuthenticated,)
    def post (self, request, format=None):
        serializer = CompanySerializer(Company.objects.get(id = request.data['id']))
        return Response(serializer.data, status = status.HTTP_200_OK)


class GetOnDemandCompany(APIView):
    permission_classes = (IsAuthenticated,)
    def get (self, request, format=None):
        serializer = GetOnDemandCompanySerialzer(Company.objects.filter(status='on_demand'), many=True)
        data = serializer.data

        return Response(serializer.data, status = status.HTTP_200_OK)



class AdList(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # queryset = list(chain(Company.objects.filter(status='ad') , Company.objects.filter(status='on_demand'))).
        li = []
        for ins in Company.objects.order_by('-id'):
            if ins.status == 'ad' or ins.status == 'call':
                li.append(AdSerializer(ins).data)
        return Response(li, status=status.HTTP_200_OK)
