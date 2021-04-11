from django.db import models

# Create your models here.
class Database2(models.Model):
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    authid = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    Pancard = models.CharField(max_length=100)
    crop = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)



    @staticmethod
    def validteuser(email, password):
        print(email, password)
        print(email, password)
        try:
            contents = Database2.objects.get(email=email, password=password)
            print(contents.email)
            return 'yes'
        except Database2.DoesNotExist:
            return 0

class FirstDB1(models.Model):
    State=models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Crop = models.CharField(max_length=50)
    Org=models.FloatField()
    Pred=models.FloatField()

