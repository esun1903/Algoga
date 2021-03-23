from django.db import models

# Create your models here.
class User(models.Model):
    user_seq = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_baek_id = models.CharField(max_length=50, blank=True, null=True)
    user_nickname = models.CharField(max_length=50)
    user_profile_image = models.CharField(max_length=500)
    user_register_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
