from django.db import models

# Create your models here.


class Tag(models.Model):
    tag_text = models.CharField(max_length=128)

    def __str__(self):
        return self.tag_text


class Status(models.Model):
    status_text = models.CharField(max_length=128)

    def __str__(self):
        return self.status_text


class Question (models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    submitter = models.CharField(max_length=128)
    submitDate = models.DateTimeField('date submitted')
    tags = models.ManyToManyField(Tag,through="QuestionTag")
    status = models.ForeignKey(Status)

    def __str__(self):
        return self.title


class QuestionTag(models.Model):
    question = models.ForeignKey(Question)
    tag = models.ForeignKey(Tag)
