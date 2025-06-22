from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Message

@login_required
def delete_user(request):
    user = request.user
    logout(request)  # Log out the user before deletion
    user.delete()    # Triggers post_delete signal
    return redirect('home')  # Replace 'home' with your homepage URL name

@login_required
def threaded_messages_view(request):
    messages = Message.objects.filter(parent_message__isnull=True, sender=request.user)\
        .select_related('sender')\
        .prefetch_related('replies__sender')

    return render(request, 'messaging/threaded_messages.html', {'messages': messages})