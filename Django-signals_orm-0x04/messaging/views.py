from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models import Prefetch
from .models import Message

def get_user_conversations(user):
    root_messages = (
        Message.objects.filter(receiver=user, parent_message__isnull=True)
        .select_related('sender', 'receiver')
        .prefetch_related(
            Prefetch('replies', queryset=Message.objects.select_related('sender'))
        )
        .order_by('-timestamp')
    )
    return root_messages

def get_threaded_replies(message):
    replies = message.replies.select_related('sender').all()
    result = []
    for reply in replies:
        nested = get_threaded_replies(reply)
        result.append({'message': reply, 'replies': nested})
    return result

def get_full_conversation(message):
    return {
        'message': message,
        'replies': get_threaded_replies(message)
    }

def get_all_conversations(user):
    return [get_full_conversation(msg) for msg in get_user_conversations(user)]


@login_required
def delete_user(request):
    user = request.user
    logout(request)
    user.delete()  # Required for the check
    return redirect('home')  # Replace 'home' with your desired redirect URL

# Create your views here.
