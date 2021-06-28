from django.contrib import admin
from .models import *

admin.site.register(student)
admin.site.register(tutor)
admin.site.register(session)
admin.site.register(status)
admin.site.register(education_level)
admin.site.register(subject)