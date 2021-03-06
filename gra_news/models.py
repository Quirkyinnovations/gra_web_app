from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    auth = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.auth
    
class SportNews(models.Model):
    auth = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.auth