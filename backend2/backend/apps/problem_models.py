from django.db import models

# Create your models here.
class User_Problem(models.Model):
    user_problem_seq = models.IntegerField(max_length=50)  #사용자 푼 문제 seq
    user_problem_correct = models.BooleanField(default=False) #사용자 seq
    problem_problem_seq = models.IntegerField(max_length=100) #문제 seq
    user_user_seq = models.IntegerField(max_length=100) #정답/오답

    class Meta:
        managed = False
        db_table = 'user_problem'