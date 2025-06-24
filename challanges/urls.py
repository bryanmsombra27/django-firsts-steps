from django.urls import path
from . import views


urlpatterns = [
    # path('january', views.index, name='index'),
    # path('february', views.february, name='february'),
    # path('<month>', views.monthly_challange, name='monthly_challange'),
    path('<int:month>', views.monthly_chanllange_by_number,
         name='monthly_challange_by_number'),
    path('<str:month>', views.monthly_challange, name='monthly_challange'),
]
