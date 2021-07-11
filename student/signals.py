'''from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import student_account
from django.contrib.auth.models import Group

def student_profile(sender, instance, created, **kwargs):
    if created:
        student_group = Group.objects.get(name='student')
        instance.groups.add(student_group)
        student_account.objects.create(
            user=instance,
            name=instance.username,
        )
        print('account created')
        print("gorep")
        print(student_group)

post_save.connect(student_profile, sender=User)'''