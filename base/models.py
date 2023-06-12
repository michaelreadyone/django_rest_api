from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Var(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    
class DOE(models.Model):
    name = models.CharField(max_length=100)
    goal = models.TextField()
    reference = models.TextField(null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
class DOEvar(models.Model):
    doe_id = models.ForeignKey(DOE, on_delete=models.CASCADE)
    var_id = models.ForeignKey(Var, on_delete=models.CASCADE)
    levels = models.IntegerField()
    unit = models.CharField(max_length=100)
    
class Varlevel(models.Model):
    doe_var_id = models.ForeignKey(DOEvar, on_delete=models.CASCADE)
    level = models.IntegerField()
    value_num = models.FloatField(null=True, default=0.0)
    
class DOErun(models.Model):
    run_number = models.IntegerField()
    level_id = models.ForeignKey(Varlevel, on_delete=models.CASCADE)
