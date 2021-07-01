from django.forms import ModelForm
from .models import *

class sessionform(ModelForm):
    class Meta:           #define which models, and which fields to use
        model = session
        fields = '__all__'  #otherwise ['date', 'time'] for only date and time