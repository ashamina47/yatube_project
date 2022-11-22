from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index.html', views.index, name = 'home_page'),
    path('group/<slug:slug>/', views.group_posts, name = 'group_list'),
    
]