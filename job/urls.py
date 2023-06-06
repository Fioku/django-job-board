from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.read_jobs),
    path('<int:id>', views.job_detail),
]
