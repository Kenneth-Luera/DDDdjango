import time
import logging

logger = logging.getLogger("django")

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = round((time.time() - start_time) * 1000, 2)

        logger.info(
            f"{request.method} {request.path} "
            f"status={response.status_code} "
            f"time={duration}ms "
            f"ip={self.get_client_ip(request)}"
        )

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")
