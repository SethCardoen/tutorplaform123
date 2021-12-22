from django.contrib import admin
from .models import *

admin.site.register(status)
admin.site.register(education_level)
admin.site.register(subject)
admin.site.register(LanguageChoice)
admin.site.register(LessonFormat)
#admin.site.register(OpenSlot)
admin.site.register(LessonRequest)