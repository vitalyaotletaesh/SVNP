from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('project/list/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    path('file/upload/', views.file_upload, name='file_upload'),
    url(r'^logout/$', views.user_logout, name='logout'),
]
