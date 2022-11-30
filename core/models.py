from django.db import models
# Create your models here.
class Todo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(default=False)
def __str__(self):
        return self.Title
class Inventory(models.Model):
    Item =  models.CharField(max_length=999,blank=False)
    Quantity= models.IntegerField( blank=False)
    Price= models.IntegerField(blank=False)
def __str__(self):
        return self.Item
class BarnMgt(models.Model):
    Product= models.CharField(max_length=9999,blank=False)
    Quantity= models.IntegerField(blank=False)
    Price= models.IntegerField(blank=False)
def __str__(self):
     return self.Product

class Profile(models.Model):
    Name = models.CharField(max_length=90,blank=False)
    Length = models.IntegerField(blank=False)
    Breadth = models.IntegerField(blank=False)
    Email = models.EmailField(max_length=999,blank=False)
    Phone_no = models.IntegerField(blank=False)
    Tags = models.CharField(max_length=10,blank=False)
def __str__(self):
    return self.Name