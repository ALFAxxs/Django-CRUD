from django.urls import path
from . import views

urlpatterns = [
    path('ofv/', views.OrderFormView, name='order_url'),
    path('sv/', views.ShowOrderView, name='show_url'),
    path('up/<int:id>', views.UpdateOrderView, name='update_url'),
    path('del/<int:id>', views.DeleteOrderView, name='delete_url'),
]