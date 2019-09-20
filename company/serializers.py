from rest_framework import serializers
from django.contrib.auth.models import User

from . models import Company


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'name', 'type', 'detail',]


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"

class GetOnDemandCompanySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'type', 'detail','fee_count']
