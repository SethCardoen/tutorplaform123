# Generated by Django 3.2.3 on 2021-11-15 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_account_linked_tutors'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]
