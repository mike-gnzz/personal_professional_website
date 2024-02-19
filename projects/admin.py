from django.contrib import admin

# Register your models here.
from django.contrib import admin
from projects.models import Project
from projects.models import Contributions

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributions)
