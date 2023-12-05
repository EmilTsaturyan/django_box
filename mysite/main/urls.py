from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('class/', views.clas, name='clas'),
    path('blog/', views.blog, name='blog')
]
