from django.db import models

# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=50 , null=False , blank=False)
    email = models.EmailField(default='admin@gmail.com')
    pin = models.IntegerField(default='222222')
    address = models.CharField(max_length=300 , default= 'Mumbai')
    phone = models.IntegerField(default='123')
    # city = models.CharField(max_length=50 , default= 'Mumbai')
    comment = models.CharField(max_length=250 , default= 'No comments')


    def __str__(self):
        return self.name

