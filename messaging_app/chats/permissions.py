# I want to create the permissions for the chats app that allows users to view and send messages in a chat only if they are a member of that chat.
# # messaging_app/chats/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsParticipantOfConversation(BasePermission):
   
    """
    Custom permission to allow only participants of a conversation
    to access the messages.
    """

    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for all users
        return request.user and request.user.is_authenticated


    def has_object_permission(self, request, view, obj):
        # Check if the user is a participant in the conversation
        return request.user in [obj.sender, obj.receiver]