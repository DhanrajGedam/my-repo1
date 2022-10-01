from django.shortcuts import render
from myapp.models import Employee
def myview(request):
    res=Employee.objects.all()
    d={'key':res}
    return render(request,'myapp/index.html',d)


# Create your views here.
