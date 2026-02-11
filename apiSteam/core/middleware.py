import logging
import time

logger = logging.getLogger("django")

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = round((time.time() - start_time) * 1000, 2)

        logger.info(
            "HTTP request",
            extra={
                "method": request.method,
                "path": request.get_full_path(),
                "status_code": response.status_code,
                "duration_ms": duration,
            },
        )

        return response
