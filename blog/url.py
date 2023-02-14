from django.urls import path
from .views import BlogPageView, BlogDetailView
from . import views


urlpatterns = [    
    
    path( '<int:pk>', BlogDetailView.as_view(), name='post'),
    path( '', BlogPageView.as_view(), name='index'),
    #path( 'about/', views.about, name='about'),
    
]


