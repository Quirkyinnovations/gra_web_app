from django.db import models

# Create your models here.  
class Language(models.Model):
    lang = models.CharField(max_length=30)
    prefix = models.CharField(max_length=5)
    
    def __str__(self):
        return self.lang
        
class Pastor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    genre = models.CharField(max_length=5)
    nationality = models.CharField(max_length=30)
    status_matrim = models.CharField(max_length=30)
    wife_name= models.CharField(max_length=30)
    children_num = models.CharField(max_length=30)
    language = models.ManyToManyField(Language)
    
    def __str__(self):
        return self.first_name, self.last_name
    
class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
class Branche(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    pastor = models.OneToOneField(Pastor, on_delete=models.CASCADE)
    # sub_pastor = models.ManyToManyField(Pastor)
    
    def __str__(self):
        return self.place.name, self.pastor.first_name, self.pastor.last_name
