from django.urls import path
from tracks.views import tracks_index
urlpatterns = [

    ################# students
   path('index', tracks_index, name='tracks.index'),

]
