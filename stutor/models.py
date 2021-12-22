from enum import Enum

from django.db import models
from datetime import datetime
from djmoney.models.fields import MoneyField


class LessonFormat(models.Model):
    type = models.CharField(max_length=300)

    def __str__(self):
        return self.type, " (id:" + str(self.id) + ")"

class LanguageChoice(models.Model):
    language = models.CharField(max_length=300)

    def __str__(self):
        return self.language, " (id:" + str(self.id) + ")"

class subject(models.Model):
    subject = models.CharField(max_length=300)

    def __str__(self):
        return self.subject, " (id:" + str(self.id) + ")"

class education_level(models.Model):
    education_levels = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.education_levels, " (id:" + str(self.id) + ")"

class status(models.Model):
    current_status = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.current_status, " (id:" + str(self.id) + ")"

class LessonRequest(models.Model):
    lessonrequest_id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.now)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, null=False)
    education_level = models.ForeignKey(education_level, null=False, on_delete=models.CASCADE)
    lessonformat = models.ForeignKey(LessonFormat, null=False, on_delete=models.CASCADE)
    number_lessons = models.IntegerField(null=False)
    remarks = models.TextField(null=True)

'''
# blog/models.py
class BlogContributor(models.Model):
contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
contribution = models.CharField(max_length=255, blank=True)

class Meta:
unique_together = ('contributor', 'blog')
'''










