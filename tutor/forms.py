from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class create_tutor_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']