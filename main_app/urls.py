from django.urls import path
from .views import TaskDetail, TaskList
from . import views


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
]