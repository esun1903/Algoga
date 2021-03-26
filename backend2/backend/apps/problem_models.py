from django.db import models
from django.utils import timezone

# Create your models here.
class User_Problem(models.Model):
    seq = models.AutoField(primary_key=True)
    correct = models.IntegerField(max_length=50)  #정답/오답 
    problem_seq = models.IntegerField(max_length=100) #문제 seq
    user_seq = models.IntegerField(max_length=100)  #사용자 seq

    class Meta:
        managed = False
        db_table = 'user_problem'
