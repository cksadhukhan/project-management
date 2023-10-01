from django.urls import path
from . import views

urlpatterns = [
    path('', views.Projects.as_view()),
    path('<str:pk>', views.ProjectDetail.as_view())
]