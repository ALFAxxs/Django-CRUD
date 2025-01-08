from django.urls import path
from . import views

urlpatterns = [
    path('order_all/', views.OrderFormView, name='order_url'),
    path('', views.ShowOrderView, name='show_url'),
    path('update/<int:id>', views.UpdateOrderView, name='update_url'),
    path('delete/<int:id>', views.DeleteOrderView, name='delete_url'),
]