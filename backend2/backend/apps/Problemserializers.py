from django.contrib.auth.models import *
from rest_framework import serializers
from .models import *

class Problemserializers(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'

