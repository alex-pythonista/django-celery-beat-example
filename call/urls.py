from django.urls import path

from .views import EmailAPIView, CallAPIView

urlpatterns = [
    path('email/', EmailAPIView.as_view()),
    path('call/', CallAPIView.as_view()),
]