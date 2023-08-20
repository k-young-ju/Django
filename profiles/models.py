from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    #on_delete 는 User 객체가 제거되면 Profile객체도 같이 제거된다.
    image = models.ImageField(upload_to='profile/',null=True)
    #image의 경로는 /media/profile이다.
    nickname = models.CharField(max_length=20,unique=True,null=True)
    message = models.CharField(max_length=100,null=True)