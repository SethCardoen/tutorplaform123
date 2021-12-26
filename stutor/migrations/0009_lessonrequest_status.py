# Generated by Django 3.2.3 on 2021-12-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stutor', '0008_lessonrequest_student_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonrequest',
            name='status',
            field=models.CharField(choices=[('ok', 'Ok'), ('pending', 'Pending'), ('failed', 'Failed')], default='pending', max_length=255),
        ),
    ]
