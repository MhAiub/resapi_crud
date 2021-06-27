from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.add_info),
    path('api/get/<id>/',views.retrive_data),
    path('api/delete/<id>/',views.delete_data),
    path('api/update/<id>/',views.update_data),
]