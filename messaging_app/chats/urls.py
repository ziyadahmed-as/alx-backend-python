# This file defines the URL patterns for the chats app in a Django project.
# messaging_app/messaging_app/chats/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter  # NestedDefaultRouter added
from .views import ConversationViewSet, MessageViewSet

# Base router for top-level resources
router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Nested router to nest messages under conversations
conversation_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# Combine all URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversation_router.urls)),  #  Include nested routes
]
