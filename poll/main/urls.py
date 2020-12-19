from django.urls import path
from main import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('question/<int:pk>', views.Question.as_view(), name='question')
]