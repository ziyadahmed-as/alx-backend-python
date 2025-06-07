# I want to create the permissions for the chats app that allows users to view and send messages in a chat only if they are a member of that chat.
# messaging_app/chats/permissions.py

from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only participants of a conversation
    to access the messages.
    """

    def has_permission(self, request, view):
        # Allow authenticated users only
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if the user is a participant in the conversation
        is_participant = request.user in [obj.sender, obj.receiver]

        # Allow GET, HEAD, OPTIONS (SAFE_METHODS) and also PUT, PATCH, DELETE if the user is a participant
        if request.method in SAFE_METHODS or request.method in ['PUT', 'PATCH', 'DELETE']:
            return is_participant

        return False
