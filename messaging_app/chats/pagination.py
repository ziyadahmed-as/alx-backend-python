# chats/pagination.py
from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        # You can access the total count of objects here using:
        total_count = self.page.paginator.count

        # Return the paginated response including total count
        return super().get_paginated_response(data)
