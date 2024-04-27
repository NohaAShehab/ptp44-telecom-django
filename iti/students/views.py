from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
import json

from students.models import Student
from students.forms import StudentForm


# Create your views here. #
# define view as a function



# handle http request
def hello(request):
    return HttpResponse("<h1 style='text-align:center;color:red'> Hello World! from my student appliction </h1>")


def aboutus(request):
    return HttpResponse("<h2 style='text-align:center;'> About us page</h2>")


def landing(request):
    return HttpResponse("<h1 style='text-align:center;color:green'> Welcome to ITI website </h1>")




students = [
    {"id": 1, "name": "Ahmed", "age": 23, "pic": "pic1.png"},
    {"id": 2, "name": "Bob", "age": 23, "pic": "pic2.png"},
    {"id": 3, "name": "Alice", "age": 23, "pic": "pic3.png"},
    {"id": 4, "name": "Bob", "age": 23, "pic": "pic4.png"},
    {"id": 5, "name": "Alice", "age": 23, "pic": "pic5.png"},
]


def students_list(request):
    return HttpResponse(students)


def student_info(request, id ):
    print(f"id={id}", type(id))
    allstudents = filter(lambda student: student["id"] == id, students) # filter object
    allstudents= list(allstudents)
    if allstudents:
        std = json.dumps(allstudents[0])
        return HttpResponse(std)
    return HttpResponse("Student not found")



def students_landing(request):
    # return template ?
    return render(request, "students/landing.html",
                  context = {"name":"noha", "students":students})




# define function index --> get data from db

def index(request):
    students = Student.objects.all()
    return  render(request, 'students/index.html',
                   context={'students':students})


def show(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, pk=id)
    return render(request, 'students/show.html',
                  context={'student':student})



def delete(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, pk=id)
    student.delete()
    #
    url = reverse("students.index") # accept urlname
    return redirect(url)


# def create(request):
#     print(request)
#     form = StudentForm()
#     # request -> post ---> accept data then create new student
#     if request.method == "POST":
#         print(request.POST)
#         student = Student()
#         student.name = request.POST["name"]
#         student.age = request.POST["age"]
#         student.grade = request.POST["grade"]
#         student.email=request.POST["email"]
#         student.save()
#         url = reverse("students.index")  # accept urlname
#         return redirect(url)
#         # return HttpResponse("student saved")
#
#     return render(request,
#                   'students/create.html'
#                 ,context={'form':form})
#
#
#

def create(request):
    print(request)
    form = StudentForm()
    # request -> post ---> accept data then create new student
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(cleaned_data)
            # student = Student()
            # student.name = cleaned_data["name"]
            # student.age = cleaned_data["age"]
            # student.grade = cleaned_data["grade"]
            # student.email=cleaned_data["email"]
            # student.save()
            student = Student(**cleaned_data)
            student.save()
            url = reverse("students.index")  # accept urlname
            return redirect(url)
    return render(request,
                  'students/create.html'
                ,context={'form':form})








