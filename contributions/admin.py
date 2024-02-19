from django.contrib import admin
from contributions.models import Contributions

# Register your models here.

class ContributionsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contributions,ContributionsAdmin)