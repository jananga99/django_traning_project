from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn),
    path('signup/', views.signUp, name="signup"),
    path('signout/', views.signOut, name="log")
]
