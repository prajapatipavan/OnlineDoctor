from django.db import models


# Create your models here.
class paisent(models.Model):
    name=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=11,null=True)
    Email=models.EmailField(null=True)
    age=models.IntegerField()
    city=models.CharField(max_length=10,null=True)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table ="paisent"