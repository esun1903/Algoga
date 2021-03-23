from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        user = User.objects.all()
        model = User
        fields = '__all__'
        #{'email','password','baek_id','nickname','profile_image','register_date',}
   


    