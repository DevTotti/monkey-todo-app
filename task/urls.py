from django.urls import path
from .views import TodoView, TodoRetrieveView


urlpatterns = [
    path('<user_id>/create/', TodoView.as_view()),
    path('<user_id>/', TodoRetrieveView.as_view()),
    path('<user_id>/<todo_id>/', TodoRetrieveView.as_view()),
]