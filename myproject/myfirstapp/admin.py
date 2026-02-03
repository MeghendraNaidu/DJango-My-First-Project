from django.contrib import admin
from myfirstapp.models import userProfile

# Register your models here.

class userProfile_admin(admin.ModelAdmin):
    list_display = ['name', 'age', 'city']
    # ordering = ['name']
    
admin.site.register(userProfile, userProfile_admin)

