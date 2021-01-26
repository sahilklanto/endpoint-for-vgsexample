from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path

router = DefaultRouter()

urlpatterns = [
    path('', views.DummyView.as_view(), name='dummy-view')
]

# urlpatterns += router.urls
