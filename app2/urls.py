from django.urls import include,path
from app2.views import *
app_name='something'

urlpatterns=[
    path('task/',task,name='task'),
    path('hello/',hello,name='hello'),
]