from django.urls import path
from . import views
from .views import AuthorListCreateView, AuthorDetailView

urlpatterns = [
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

]
    