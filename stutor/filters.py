import django_filters
from .models import *
from django_filters import DateFilter

class session_filter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte') # find a date that is greater than or equal to date
    end_date = DateFilter(field_name="date", lookup_expr='lte') # find a date that is greater than date (models)

    class Meta:
        model = session
        fields = ['student', 'subject']

