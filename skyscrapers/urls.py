from django.urls import path
from .views import SkyscraperList, SkyscraperDetail

urlpatterns = [
    path('', SkyscraperList.as_view(), name='sky_list'),
    path('<int:pk>/', SkyscraperDetail.as_view(), name='sky_detail'),
]

