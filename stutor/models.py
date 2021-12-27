from django.db import models
from datetime import datetime


class LessonFormat(models.Model):
    type = models.CharField(max_length=300)

    def __str__(self):
        return self.type

class LanguageChoice(models.Model):
    language = models.CharField(max_length=300)

    def __str__(self):
        return self.language

class subject(models.Model):
    subject = models.CharField(max_length=300)

    def __str__(self):
        return self.subject

class education_level(models.Model):
    education_levels = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.education_levels

class status(models.Model):
    current_status = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.current_status

class LessonRequest(models.Model):
    OPEN = 'open'
    PENDING = 'pending'
    PROCESSED = 'processed'

    STATUS = (
        (OPEN, 'open'),
        (PENDING, 'Pending'),
        (PROCESSED, 'processed'),
    )

    lessonrequest_id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.now)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, null=False)
    education_level = models.ForeignKey(education_level, null=False, on_delete=models.CASCADE)
    lessonformat = models.ForeignKey(LessonFormat, null=False, on_delete=models.CASCADE)
    number_lessons = models.IntegerField(null=False)
    remarks = models.TextField(blank=True,null=True)
    student_account = models.ForeignKey(to='student.student_account', null=False, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS, default=OPEN)














