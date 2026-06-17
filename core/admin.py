from django.contrib import admin

from .models import ContactMessage, Experience, Project, Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "order")
    list_filter = ("category",)
    list_editable = ("proficiency", "order")
    search_fields = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date", "is_current", "order")
    list_filter = ("is_current",)
    list_editable = ("order",)
    search_fields = ("role", "company")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "order")
    list_editable = ("featured", "order")
    list_filter = ("featured",)
    search_fields = ("title", "description", "tags")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "read")
    list_filter = ("read", "created_at")
    readonly_fields = ("name", "email", "message", "created_at")
    search_fields = ("name", "email", "message")
