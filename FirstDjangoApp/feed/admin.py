from django.contrib import admin
from .models import Posts

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posts, PostAdmin)
