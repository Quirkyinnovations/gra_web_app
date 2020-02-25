from django.contrib import admin
from .models import Place, Branche,Pastor,Language

# Register your models here.
admin.site.register(Pastor)
admin.site.register(Place)
admin.site.register(Branche)
admin.site.register(Language)
