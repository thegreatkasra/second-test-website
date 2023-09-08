from django.http import HttpResponseRedirect
from django.urls import reverse

class RedirectToSplashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path != reverse('splash_page'):
            return HttpResponseRedirect(reverse('splash_page'))
        return self.get_response(request)
