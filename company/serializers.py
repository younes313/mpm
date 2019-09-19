from rest_framework import serializers
from django.contrib.auth.models import User

from . models import Company


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'name', 'type', 'detail',]
