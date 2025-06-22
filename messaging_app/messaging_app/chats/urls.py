# chats/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet

# Main router for top-level routes (conversations)
router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Nested router for messages under conversations
conversation_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# Combine all URL patterns
urlpatterns = [
    path('', include(router.urls)),                # /api/chats/conversations/
    path('', include(conversation_router.urls)),   # /api/chats/conversations/<id>/messages/
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
