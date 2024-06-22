from django.urls import path, include
from .views import (
    TodoListApiView,
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
]
path('api/todos/', TodoListApiView.as_view(), name='todo-list'),
path('api/todos/<int:pk>/', TodoListApiView.as_view(), name='todo-detail'),
