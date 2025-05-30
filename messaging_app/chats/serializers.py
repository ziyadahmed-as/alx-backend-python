from rest_framework import serializers
from .models import User, Conversation, Message

# User Serializer to serialize User model
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()  # Demonstrates use of SerializerMethodField

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

# Message Serializer to serialize Message model
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    message_body = serializers.CharField()  # Demonstrates use of CharField

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at']

    def validate_message_body(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")  # Demonstrates ValidationError
        return value

# Conversation Serializer to serialize Conversation model
class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages', 'created_at']
