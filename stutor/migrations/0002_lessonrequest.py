# Generated by Django 3.2.3 on 2021-12-22 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stutor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonRequest',
            fields=[
                ('lessonrequest_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
