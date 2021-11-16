from django.shortcuts import render
from .forms import studentregistration
from .models import user
from django.http import HttpResponseRedirect

# Create your views here.

def addshow(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm,email =em,password = pw)
            reg.save()
            fm = studentregistration()
    else:
        fm = studentregistration()
    
    stud = user.objects.all()
    return render(request, 'add.html',{'form' :fm,'stu':stud})

def delete_data(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    if request.method == 'POST':
         pi = user.objects.get(pk = id)
         fm = studentregistration(request.POST,instance=pi)  
         if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk = id)
        fm = studentregistration(instance=pi)
        return render(request,'update.html',{'form':fm})
    return render(request,'update.html',{'form':fm})
          