from django.contrib import admin
from .models import Education, Name  # Import your models

# Register your models here
admin.site.register(Education)
admin.site.register(Name)