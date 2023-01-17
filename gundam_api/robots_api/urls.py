from django.urls import path
from .import views

urlpatterns = [
    path('api/gundam', views.GundamList.as_view(), name='gundam_list'),
    path('api/gundam/<int:pk>', views.GundamDetail.as_view(), name='gundam_detail')
]