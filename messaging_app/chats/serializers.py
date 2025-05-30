#
from rest_framework import serializers
from .models import User, Conversation, Message

#User Serializer to serialize User model by using ModelSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# Message Serializer to serialize Message model by using ModelSerializer
class MessageSerializer(serializers.ModelSerializer):
    # this is make sender field read-only and use UserSerializer to serialize the sender
    sender = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['id', 'sender', 'text', 'timestamp']

class ConversationSerializer(serializers.ModelSerializer):
    # the following fields are serialized using UserSerializer and MessageSerializer
    # to make them read-only
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages', 'created_at']