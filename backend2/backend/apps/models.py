from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    seq = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    baek_id = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=500, blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'user'


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Problem(models.Model):
    seq = models.AutoField(primary_key=True)
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    correct_user = models.IntegerField()
    submission_cnt = models.IntegerField()
    correct_rate = models.FloatField()
    level = models.IntegerField()
    avg_try = models.FloatField()

    class Meta:
        managed = False
        db_table = 'problem'


class UserProblem(models.Model):
    problem_seq = models.OneToOneField(Problem, models.DO_NOTHING, db_column='problem_seq', primary_key=True)
    user_seq = models.ForeignKey(User, models.DO_NOTHING, db_column='user_seq')
    correct = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_problem'
        unique_together = (('problem_seq', 'user_seq'),)