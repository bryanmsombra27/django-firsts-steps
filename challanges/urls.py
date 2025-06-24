from django.urls import path
from . import views


urlpatterns = [
    # path('january', views.index, name='index'),
    # path('february', views.february, name='february'),
    path('<month>', views.monthly_challange, name='monthly_challange'),
]
