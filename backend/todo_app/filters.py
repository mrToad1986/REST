from django_filters import BooleanFilter, CharFilter, DateTimeFilter, DateTimeFromToRangeFilter
from django_filters.widgets import BooleanWidget, RangeWidget
from django_filters.rest_framework import FilterSet
from .models import Project, TODO

class ProjectFilter(FilterSet):
    name = CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']

class TODOFilter(FilterSet):
    project_id = CharFilter(lookup_expr='contains')
    created_at = DateTimeFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}))
    is_active = BooleanFilter(widget=BooleanWidget())

    class Meta:
        model = TODO
        fields = ['project_id', 'created_at', 'is_active']