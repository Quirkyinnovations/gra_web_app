from django.db import models
from django.utils import timezone

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('title',)
        

class Blog(models.Model):
    headline = models.CharField(max_length=300)
    body = models.TextField(null=True)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now())
    publications = models.ManyToManyField(Publication)
    
    def __str__(self):
        return self.headline
        
    # custom short text
    def shortenText(self):
        return self.body[:100]
        
    class Meta:
        ordering = ('headline',)
