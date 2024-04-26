from django.shortcuts import render
from django.http import HttpResponse

import json


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
    return render(request, "students/landing.html")






