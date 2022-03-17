# Added this file.
from django.urls import path, include
from . import views

urlpatterns = [
    # For the HTML format:
    path('signup', views.signup, name = 'signup'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('home', views.home, name = 'home'),
    # For the JSON format:
    path('cats', views.ListCat.as_view()),
    path('cats/<int:pk>', views.DetailCat.as_view()),
]
