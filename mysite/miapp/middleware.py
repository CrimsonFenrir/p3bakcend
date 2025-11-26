import logging
from django.shortcuts import render

logger = logging.getLogger('miapp')

class ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception as e:
            logger.error(f"Error global: {e}", exc_info=True)
            return render(request, 'error.html', {"mensaje": "Ha ocurrido un error inesperado"})
