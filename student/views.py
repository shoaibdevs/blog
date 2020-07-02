from django.shortcuts import render, redirect
from .models import Student, Result
from .forms import StudentForm, ResultForm

# Create your views here.


def create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/first-class')
            except:
                pass
    else:
        form = StudentForm()
    return render(request,'student/create_student.html',{'form':form})

def add(request):

    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/first-class')
            except:
                pass
    else:
        form = ResultForm()
    return render(request,'student/result.html',{'form':form})


def show(request):

    students = Student.objects.all()

    return render(request,"student/1.html",{'students':students})

def result(request):
    
    data = Result.objects.all()

    return render(request, 'student/1-result.html', {data : 'result'})
    


def delete(request, id):

    students = Student.objects.get(id=id)
    students.delete()

    return redirect("/table")