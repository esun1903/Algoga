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

class ProblemCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem_Custom
        fields = '__all__'

class CodeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeBoard
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProblem
        fields = '__all__'

class FollowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUser
        fields = '__all__'

class FollowingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUser
        fields = '__all__'

class FollowerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUser
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = '__all__'