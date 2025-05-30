# this used to define the URL patterns for the chats app in a Django project.
# messaging_app/messaging_app/chats/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)

# The urlpatterns list routes URLs to views. For more information please see:
urlpatterns = [
    path('', include(router.urls)),
]