from django.contrib import admin
from Feedback.models import Question
from Feedback.models import Tag
from Feedback.models import Status
# Register your models here.


class QuestionInline(admin.TabularInline):
    model = Question


class StatusAdmin(admin.ModelAdmin):
    inlines = (QuestionInline)


class QuestionTagsInline(admin.TabularInline):
    model = Question.tags.through


class StatusInline(admin.TabularInline):
    model = Status


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Info", {'fields': ['title', 'description', 'status']}),
        ("Submit Info", {'fields': ['submitter', 'submitDate']})
    ]
    inlines = [QuestionTagsInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag)
admin.site.register(Status)