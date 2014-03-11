from django.contrib import admin
from Feedback.models import Question
from Feedback.models import Tag
from Feedback.models import Status
from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.


class QuestionInline(admin.TabularInline):
    model = Question


class StatusAdmin(admin.ModelAdmin):
    inlines = (QuestionInline)


class QuestionTagsInline(admin.StackedInline):
    model = Question.tags.through
    extra = 1


class StatusInline(admin.TabularInline):
    model = Status


class QuestionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        # models.TextField: {'widget': Textarea(attrs={'rows': 6, 'cols': 80})},
    }
    fieldsets = [
        ("Question Info", {'fields': ['title', 'description', 'status']}),
        ("Submit Info", {'fields': ['submitter', 'submitDate']})
    ]
    inlines = [QuestionTagsInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag)
admin.site.register(Status)