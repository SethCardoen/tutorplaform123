import django_filters
from .models import student_account
from tutor.models import tutor_account
from django_filters import ModelChoiceFilter
from django_filters.filterset import FilterSet

#class tutor_sidebar_filte(django_filters.FilterSet):
 #   teacher = ModelMultipleChoiceFilter(queryset=teacher.objects.all())
  #  class Meta:
   #     model = student_account
    #    fields = ['teacher']

#class tutor_sidebar_filt(BaseFilterSet):
 #  teacher = ModelMultipleChoiceFilter(
  #      field_name='teacher',
   #     to_field_name='tutor_account',
    #    queryset=student_account.objects.all(),
    #)

class tutor_sidebar_filter(FilterSet):
    """Filter for books by author"""
    teach = ModelChoiceFilter(queryset=tutor_account.objects.all())

    class Meta:
        model = student_account
        fields = ['teacher']