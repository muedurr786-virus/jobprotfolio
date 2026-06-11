from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):

    def __str__(self):
        return self.username
    
class UpdateProfiel(models.Model):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    user =models.OneToOneField(UserModel, on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(null=True, max_length=50)
    age = models.IntegerField(null=True)
    gender = models.CharField(null=True, max_length=50,choices=GENDER)
    height = models.FloatField(null=True, blank= True)
    weight = models.FloatField(null=True, blank=True)
    bmr = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.name
    
class FoodItemModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    calory = models.FloatField(null=True, blank=True)
    date_consumed = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name
    

