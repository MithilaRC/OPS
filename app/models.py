from django.db import models

# Create your models here.
class LoginAdminModel(models.Model):
    uname=models.CharField(max_length=30)
    pwd=models.CharField(max_length=30)
class CreatePlotModel(models.Model):
    plotno=models.IntegerField(primary_key=True)
    roadno=models.IntegerField()
    surveyno=models.IntegerField()
    cstpersqyd=models.IntegerField()
    totalsqyd=models.IntegerField()
    expenses=models.IntegerField()
    boundaries=models.IntegerField()
    facing=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    totalcost=models.IntegerField()
    img=models.ImageField(default=False)

class CreateFlattModel(models.Model):
        flatno = models.IntegerField(primary_key=True)
        roadno = models.IntegerField()
        surveyno = models.IntegerField()
        cstpersqyd = models.IntegerField()
        totalsqyd = models.IntegerField()
        expenses = models.IntegerField()
        boundaries = models.IntegerField()
        facing = models.CharField(max_length=20)
        status = models.CharField(max_length=20)
        totalcost = models.IntegerField()
        img = models.ImageField(default=False)
class CreateEmployeeModel(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    maillocation=models.EmailField()
    doj=models.DateField()
    locatio=models.CharField(max_length=30,default=False)
    role=models.CharField(max_length=30)
    qualification=models.CharField(max_length=20)
    remarks=models.CharField(max_length=30)