from django.urls import path
from .views import home, aboutus, todolist, create, delete, toggle

urlpatterns = [
    path('', home, name='home'),
    path('list/', todolist, name='task-list'),
    path('about/', aboutus, name='aboutus'),
    path('create/', create, name='task-create'),
    path('delete/<int:id>/', delete, name='task-delete'),
    path('toggle/<int:id>/', toggle, name='task-toggle'),
]