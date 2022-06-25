from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('project/list/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    #path('registration/login/', views.login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #url(r'^logout-then-login/$', views.logout_then_login, name='logout_then_login'),
    #url(r'^$', views.dashboard, name='dashboard'),
]
