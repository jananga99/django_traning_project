from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customerOrder import views

urlpatterns = [
    path('', views.CustomerOrderList.as_view()),
    path('<int:pk>/', views.CustomerOrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)