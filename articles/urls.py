from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),

    path('article/create/', views.create, name='create_article'),
    path('article/<int:pk>/update/', views.update_article, name='update_article'),
    
    path('tag/create/', views.create_tag, name='create_tag'),
    path('tag/<int:pk>/update/', views.update_tag, name='update_tag'),
]