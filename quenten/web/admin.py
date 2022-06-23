from django.contrib import admin

from .models import Adult, Directorate, Team

# Register your models here.

admin.site.register(Directorate)
admin.site.register(Team)
admin.site.register(Adult)
