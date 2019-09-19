from rest_framework import serializers
from django.contrib.auth.models import User

from . models import Funder


#
# class FunderSerializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     email = serializers.EmailField()
#     national_code = serializers.CharField()
#     phone_number = serializers.CharField()


class FundingSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    money = serializers.IntegerField()
    public_or_specefic = serializers.CharField()
    help_or_contribute = serializers.CharField()
