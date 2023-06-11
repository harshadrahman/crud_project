from django.shortcuts import render, redirect
from .models import Task
from.forms import TaskForm

# Create your views here.
def index(request):
    task1=Task.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','')
        item=request.POST.get('item_name','')
        desc=request.POST.get('desc','')
        task=Task(slno=slno,item=item,desc=desc)
        task.save()
    return render(request,'index.html',{'task1':task1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=TaskForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})





