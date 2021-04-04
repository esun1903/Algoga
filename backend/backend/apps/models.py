from django.db import models
from django.utils import timezone

# Create your models here.
class CodeBoard(models.Model):
    seq = models.AutoField(primary_key=True)
    code = models.TextField()
    explanation = models.TextField()
    free_write = models.TextField()
    public = models.IntegerField()
    register_date = models.DateTimeField(blank=True, null=True)
    like_cnt = models.IntegerField()
    language = models.CharField(max_length=45)
    user_seq = models.ForeignKey('User', models.DO_NOTHING, db_column='user_seq')
    problem_seq = models.ForeignKey('Problem', models.DO_NOTHING, db_column='problem_seq')
    language_seq = models.ForeignKey('Language', models.DO_NOTHING, db_column='language_seq')

    class Meta:
        managed = False
        db_table = 'code_board'


class Comment(models.Model):
    seq = models.AutoField(primary_key=True)
    text = models.TextField()
    register_date = models.DateTimeField()
    like_cnt = models.IntegerField()
    user_seq = models.ForeignKey('User', models.DO_NOTHING, db_column='user_seq')
    code_board_seq = models.ForeignKey(CodeBoard, models.DO_NOTHING, db_column='code_board_seq') 

    class Meta:
        managed = False
        db_table = 'comment'


class FollowUser(models.Model):
    seq = models.AutoField(primary_key=True) # , related_name = 'follower_seq'  related_name = 'following_seq'
    user_follower_seq = models.IntegerField()
    user_following_seq = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'follow_user'



class Information(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'information'


class InformationOfProblem(models.Model):
    information_seq = models.OneToOneField(Information, models.DO_NOTHING, db_column='information_seq', primary_key=True)
    problem_seq = models.ForeignKey('Problem', models.DO_NOTHING, db_column='problem_seq')       

    class Meta:
        managed = False
        db_table = 'information_of_problem'
        unique_together = (('information_seq', 'problem_seq'),)


class Language(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'language'


class Problem(models.Model):
    seq = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    correct_user = models.IntegerField()
    submission_cnt = models.IntegerField()
    correct_rate = models.FloatField()
    level = models.IntegerField()
    avg_try = models.FloatField()
    time_limit = models.CharField(max_length=50)
    memory_limit = models.CharField(max_length=50)
    algorithms = models.CharField(max_length=200, blank=True, null=True)
    algorithm_ids = models.CharField(max_length=100, blank=True, null=True)
    review_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'problem'

class Problem_Custom(models.Model):
    seq = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    correct_user = models.IntegerField()
    submission_cnt = models.IntegerField()
    correct_rate = models.FloatField()
    level = models.IntegerField()
    avg_try = models.FloatField()
    time_limit = models.CharField(max_length=50)
    memory_limit = models.CharField(max_length=50)
    algorithms = models.CharField(max_length=200, blank=True, null=True)
    algorithm_ids = models.CharField(max_length=100, blank=True, null=True)
    review_count = models.IntegerField()

    class Meta:
        managed = False

# class Problem_Custom(models.Model):
#     seq = models.AutoField(primary_key=True)
#     number = models.IntegerField()
#     name = models.CharField(max_length=100)
#     correct_user = models.IntegerField()
#     submission_cnt = models.IntegerField()
#     correct_rate = models.FloatField()
#     level = models.IntegerField()
#     avg_try = models.FloatField()
#     review_count = models.IntegerField()

#     class Meta:
#         managed = False
        
class RecommendProblem(models.Model):
    seq = models.AutoField(primary_key=True)
    recommend_user_seq = models.ForeignKey('RecommendUser', models.DO_NOTHING, db_column='recommend_user_seq')

    class Meta:
        managed = False
        db_table = 'recommend_problem'
        unique_together = (('seq', 'recommend_user_seq'),)


class RecommendUser(models.Model):
    seq = models.AutoField(primary_key=True)
    baek_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'recommend_user'


class Type(models.Model):
    seq = models.IntegerField(primary_key=True)
    id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'type'


class TypeOfProblem(models.Model):
    type_seq = models.OneToOneField(Type, models.DO_NOTHING, db_column='type_seq', primary_key=True)
    problem_seq = models.ForeignKey(Problem, models.DO_NOTHING, db_column='problem_seq')

    class Meta:
        managed = False
        db_table = 'type_of_problem'
        unique_together = (('type_seq', 'problem_seq'),)


class User(models.Model):
    seq = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    baek_id = models.CharField(max_length=50)
    nickname = models.CharField(unique=True, max_length=50)
    profile_image = models.CharField(max_length=500, blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    # is_active = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'user'


class UserProblem(models.Model):
    problem_seq = models.OneToOneField(Problem, models.DO_NOTHING, db_column='problem_seq', primary_key=True)
    user_seq = models.ForeignKey(User, models.DO_NOTHING, db_column='user_seq')
    correct = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_problem'
        unique_together = (('problem_seq', 'user_seq'),)


