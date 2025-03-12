from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Show name & URL in the admin list view
    list_display = ("name", "deployed_url")
