from django.contrib import admin
from .models import Attendance

class PostAdmin (admin.ModelAdmin):
    pass #(we can do anything here but we simply just want the post editable)

admin.site.register(Attendance, PostAdmin)



