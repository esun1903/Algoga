from django.db import models

# Create your models here.
class User(models.Model):
    seq = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    baek_id = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=500, blank=True, null=True)
    register_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
