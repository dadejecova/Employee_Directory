from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from employees.models import Employee
# Create your views here.
def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee': employee
    }	
    return render(request, 'employee_detail.html', context)