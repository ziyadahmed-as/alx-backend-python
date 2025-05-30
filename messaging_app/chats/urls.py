# This file defines the URL patterns for the chats app in a Django project.
# messaging_app/messaging_app/chats/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter  #  routers.DefaultRouter() is used here
from .views import ConversationViewSet, MessageViewSet

# Initialize DefaultRouter to automatically generate URL routes for viewsets
router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Include router-generated URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
