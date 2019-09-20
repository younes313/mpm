from rest_framework import serializers
from django.contrib.auth.models import User

from . models import *



class FunderSignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    national_code = serializers.CharField()
    phone_number = serializers.CharField()




class GetUserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Funder
        fields = ['national_code', 'phone_number']

    def to_representation(self, instance):

        representation = super().to_representation(instance)
        representation['first_name'] = instance.user.first_name
        representation['last_name'] = instance.user.last_name
        representation['email'] = instance.user.email
        return representation



class GetHistorySerialzer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ['company', 'money', 'date', 'public_or_specefic', 'help_or_contribute']

    def to_representation(self, instance):

        representation = super().to_representation(instance)
        if instance.company != None:
            representation['company_name'] = instance.company.name
            representation['invesment_percentage'] = (instance.money / instance.company.needed_fee ) * (instance.company.stock_percent / 100) * 100
        return representation

class FundingSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    money = serializers.IntegerField()
    public_or_specefic = serializers.CharField()
    help_or_contribute = serializers.CharField()
