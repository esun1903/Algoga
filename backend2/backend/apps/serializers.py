from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'

class CodeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeBoard
        fields = '__all__'

