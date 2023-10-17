from django.urls import path
from . import views

urlpatterns = [
    # Add task to databse
    path('addTask/', views.addTask, name="addTask"),
    # Mark a task as completed
    path('markAsCompleted/<int:pk>/', views.markAsCompleted, name="markAsCompleted"),
    # Mark a task as incompleted
    path('markAsIncompleted/<int:pk>/', views.markAsIncompleted, name="markAsIncompleted"),
    # Edit a task 
    path('editTask/<int:pk>/', views.editTask, name="editTask"),
    # Delete a task
    path('deleteTask/<int:pk>/', views.deleteTask, name="deleteTask"),
]