from django.contrib import admin
from .models import Reporter,Type_report,Report

# Register your models here.
admin.site.register(Reporter)
admin.site.register(Report)
admin.site.register(Type_report)

