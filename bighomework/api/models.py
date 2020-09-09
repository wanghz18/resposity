from django.db import models


# Create your models here.
class user(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    session_id = models.CharField(max_length=10, unique=True, blank=True)
    # 用户登陆状态
