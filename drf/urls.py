from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'Book', views.BookViewSet)
urlpatterns = [
    # path('',views.BookListView.as_view(), name='api')
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]