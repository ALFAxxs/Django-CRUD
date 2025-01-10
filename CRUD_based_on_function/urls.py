from django.urls import path
from . import views

app_name = 'func'

urlpatterns = [
    path('order_func/', views.OrderAddView, name='order_func'),
    path('show_order/', views.ShowOrderView, name='show_orders'),
    path('delete/<int:id>', views.DeleteOrderView, name='delete_orders'),
    path('update/<int:id>', views.UpdateOrderView, name='update_orders')
]