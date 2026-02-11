import django_filters 
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    #retrive All Employees With The Designation
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    #filter Employees By Name Contains Word
    emp_name = django_filters.CharFilter(field_name='emp_name',lookup_expr="icontains")
    #retrive All Employees Between with IDS between "Emp002" and "Emp006"
    # id = django_filters.RangeFilter(field_name='id') #based On ID
    # emp_id = django_filters.RangeFilter(field_name='emp_id') #does not Work With Id
    id_min = django_filters.CharFilter(method = 'filter_by_id_range',label='From EMP ID')
    id_max = django_filters.CharFilter(method = 'filter_by_id_range',label='To EMP ID')
    class Meta:
        model = Employee
        fields = ['designation','emp_name','id_min','id_max']

    def filter_by_id_range(self,queryset,name ,value):
        if name== 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name=='id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset

