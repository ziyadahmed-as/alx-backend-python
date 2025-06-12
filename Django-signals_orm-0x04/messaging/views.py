from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models import Prefetch
from .models import Message


@login_required
def threaded_messages_view(request):
    messages = Message.objects.filter(parent_message__isnull=True, sender=request.user)\
        .select_related('sender')\
        .prefetch_related('replies__sender')

    return render(request, 'messaging/threaded_messages.html', {'messages': messages})

@login_required
def unread_inbox_view(request):
    """ View to display unread messages in the user's inbox."""
    unread_messages = Message.unread.unread_for_user(request.user)  # exact match
    return render(request, 'messaging/unread_inbox.html', {'unread_messages': unread_messages})

def unread_messages_view(request):
    user = request.user
    unread_messages = Message.unread.unread_for_user(user).only('sender', 'content', 'timestamp')
    
    return render(request, 'messaging/unread_messages.html', {
        'messages': unread_messages
    })

def get_user_conversations(user):
    """Retrieve all root messages (conversations) for a user."""
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
