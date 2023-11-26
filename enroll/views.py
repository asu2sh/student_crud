from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
from django.http import JsonResponse


def home(request):
    fm = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'enroll/home.html', {'form': fm, 'students': stud})


def save_data(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            sid = request.POST.get('sid')
            if sid == '':
                stud = Student(name=name, email=email, password=password)
            else:
                stud = Student(name=name, email=email, password=password, id=sid)
            stud.save()
            students = Student.objects.values()
            student_data = list(students)
            return JsonResponse({'student_data': student_data, 'status': 1})
        else:
            return JsonResponse({'status': 0})

def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        stud = Student.objects.get(pk=id)
        stud.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})
    
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        stud = Student.objects.get(pk=id)
        student_data = {"id": stud.id, "name": stud.name, "email": stud.email, "password": stud.password}
        return JsonResponse(student_data)
    else:
        return JsonResponse({'status': 0})