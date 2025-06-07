# chats/filters.py
import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    sender = django_filters.CharFilter(field_name="sender__username", lookup_expr='iexact')
    receiver = django_filters.CharFilter(field_name="receiver__username", lookup_expr='iexact')
    start_time = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_time = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'start_time', 'end_time']
