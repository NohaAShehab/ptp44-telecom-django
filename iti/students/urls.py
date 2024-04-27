from django.urls import path
from students.views import (hello, aboutus, landing,
students_list,student_info, students_landing, index,show, delete)
urlpatterns = [

    ################# students
    path('helloworld',hello, name='hellofun' ),
    path('about',aboutus,name='aboutus'),
    # path('',landing,name='landing' ),
    path('students',students_list, name='students_list' ),
    path('students/<int:id>', student_info, name='students_info' ),
    path('index', students_landing,name ='students_landing' ),
    path('', index, name='students.index' ),
    path('<int:id>', show, name='students.show' ),
    path('<int:id>/delete', delete, name='students.delete'),

]
