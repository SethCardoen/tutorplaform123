# Generated by Django 3.2.3 on 2021-12-22 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stutor', '0003_lessonrequest_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonrequest',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stutor.subject'),
        ),
    ]
