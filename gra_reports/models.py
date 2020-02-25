from django.db import models
from django.utils import timezone

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    branche = models.CharField(max_length=30)
    role = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    
    
    def __str__(self):
        return self.first_name, self.last_name, self.branche, self.department
        
    
class Type_report(models.Model):
    title= models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.title
        

    
class Report(models.Model):
    headline = models.CharField(max_length=100)
    type_report = models.OneToOneField(Type_report, on_delete=models.CASCADE)#OneToOne Relationship 
    description = models.TextField(null=False)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE) #ManyToOne Relationship 
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.headline, self.report_type
        
    class Meta:
        ordering = ('headline',)
    
    