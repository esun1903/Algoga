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