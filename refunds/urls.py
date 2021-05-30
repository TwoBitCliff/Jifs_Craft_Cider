from django.urls import path
from . import views

urlpatterns = [
    path('', views.RefundList, name='refunds'),
    path('new/', views.RequestRefund, name='RequestRefund'),

]
