from django.urls import path
from .views import UserCreateAPIView, TodoCreateView, TodoCurrentView, AdminUserCreateAPIView, ManagerUserCreateAPIView, TodoCompletedView

urlpatterns = [
    path('create/', TodoCreateView.as_view()),
    path('completed/', TodoCompletedView.as_view()),
    path('createADMIN/', AdminUserCreateAPIView.as_view()),
    path('createMANAGER/', ManagerUserCreateAPIView.as_view()),
    path('createUSER/', UserCreateAPIView.as_view()),
    path('current/<int:pk>', TodoCurrentView.as_view()),
]
