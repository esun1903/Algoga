from django.contrib.auth.models import *
from rest_framework import serializers
from .models import *

class UserProblemserializers(serializers.ModelSerializer):
    class Meta:
        model = UserProblem
        fields = '__all__'

