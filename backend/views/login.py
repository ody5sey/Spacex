from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render
from django.shortcuts import reverse
from django.http import JsonResponse


class LoginView(View):

    @staticmethod
    def get(request):
        return render(request, "backend/login.html")

    @staticmethod
    def post(request):
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        captcha = request.POST.get("captcha", None)

        if request.session["valid_code"].lower() != captcha.lower():
            data = {"status": 403, "msg": "验证码错误"}
            return JsonResponse(data, safe=False)

        user = authenticate(username=username, password=password)

        if user is not None:

            # login方法实现登录
            login(request, user)

            data = {"status": 200, "url_jump": reverse("index")}
            return JsonResponse(data, safe=False)

        else:

            # res = requests.get("http://127.0.0.1:8000/get_valid_img")
            data = {"status": 403, "msg": "用户名或者是密码错误"}
            return JsonResponse(data, safe=False)
