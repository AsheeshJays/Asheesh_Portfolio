from django.urls import path
from mainApp import views

urlpatterns = [
    path('',views.IndexPage,name='indexpage'),
    path('Project/',views.ProjectPage,name='project'),
    path('Hire/',views.HireMe,name='hireme'),
]
