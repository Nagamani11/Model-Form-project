from django.shortcuts import render
from django.http import HttpResponse
from .models import EmpData
from .form import EmpDataForm


def empData(request):
    if request.method == 'GET':
        form = EmpDataForm()  #Empty forms
        return render(request, 'form.html', {'form':form})
    else:
        form1 = EmpDataForm(request.POST)     #Form with Database
        if form1.is_valid():
            form1.save()
            form = EmpDataForm()
            return render(request, 'form.html', {'form':form})
        else:
            return HttpResponse('Invalid Form')
