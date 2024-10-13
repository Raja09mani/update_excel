from django.db import models

class StudDetail(models.Model):
    sid = models.AutoField(primary_key=True)  # Assuming sid is an AutoField
    roll = models.IntegerField()
    sname = models.CharField(max_length=30)
    sclass = models.IntegerField()
    saddress = models.CharField(max_length=100)
    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    socialscience = models.IntegerField()