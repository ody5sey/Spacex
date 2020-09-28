from django.http import HttpResponse
from django.views.generic import View


class LoginView(View):

    @staticmethod
    def get(request):
        # <view logic>
        return HttpResponse('result')
