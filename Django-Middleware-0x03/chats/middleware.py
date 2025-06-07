# chats/middleware.py
from datetime import datetime, timedelta
from django.http import JsonResponse
import time
import logging
from collections import defaultdict

# Logger for request logging (optional if reused from previous tasks)
request_logger = logging.getLogger("request_logger")
request_handler = logging.FileHandler("requests.log")
request_formatter = logging.Formatter('%(message)s')
request_handler.setFormatter(request_formatter)
request_logger.addHandler(request_handler)
request_logger.setLevel(logging.INFO)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        request_logger.info(log_message)

        return self.get_response(request)

# restrict access to chat functionality between 6 PM and 9 PM
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now().time()
        # Deny access if not between 6 PM and 9 PM
        if not (now >= datetime.strptime("18:00", "%H:%M").time() and
                now <= datetime.strptime("21:00", "%H:%M").time()):
            return JsonResponse(
                {"error": "Access to chat is restricted between 9PM and 6PM."},
                status=403
            )
        return self.get_response(request)


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Store message timestamps by IP
        self.message_logs = defaultdict(list)

    def __call__(self, request):
        # Only apply rate limit to chat POST requests
        if request.path.startswith("/api/messages/") and request.method == "POST":
            ip = self.get_client_ip(request)
            current_time = time.time()

            # Remove timestamps older than 60 seconds
            self.message_logs[ip] = [t for t in self.message_logs[ip] if current_time - t < 60]

            if len(self.message_logs[ip]) >= 5:
                return JsonResponse(
                    {"error": "Message limit exceeded. Try again in a minute."},
                    status=403
                )

            self.message_logs[ip].append(current_time)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")
