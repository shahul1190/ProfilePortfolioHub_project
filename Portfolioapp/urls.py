from django.urls import path
from . import views
from .views import create_profile


urlpatterns = [
    path("", views.indextwo, name='apple'),
    path('home/', views.home_view, name='home'),
    path('portfolio/', views.project_detail, name='project_detail'),

    path('port_create/', views.project_create, name='project_create'),
    path('port_edit/', views.project_edit, name='project_edit'),
    path('profile/', views.profile_view, name='user_profile'),
    path('create_profile/', create_profile, name='create_profile'),
    path('edit_profile/', views.profile_edit, name='edit_profile'),
]

