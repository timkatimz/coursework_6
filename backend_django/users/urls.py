from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter


# Register user router
users_router = SimpleRouter()
users_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(users_router.urls)),
    path('', include('djoser.urls.jwt')),
]