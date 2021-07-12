# Generated by Django 3.2 on 2021-07-12 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stutor', '0003_auto_20210712_1731'),
        ('student', '0002_auto_20210712_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_account',
            name='student_education_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stutor.education_level'),
        ),
        migrations.AddField(
            model_name='student_account',
            name='student_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stutor.subject'),
        ),
    ]
