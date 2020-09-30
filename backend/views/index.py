from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt

from librarys.mixin.permission import LoginRequiredMixin
from backend.models.users import Users


class IndexView(LoginRequiredMixin, View):
    template_name = "backend/index.html"
    title = "管理"

    def get(self, request):
        user_id = Users.objects.filter(username="luffy").first()
        if not user_id:
            Users.objects.create_user(username="luffy", password="shadow", is_superuser=True)

        return render(request, self.template_name, {'title': self.title})


class LogoutView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        logout(request)
        data = {"status": 200}
        return JsonResponse(data, safe=False)


class ChangeView(LoginRequiredMixin, View):
    template_name = "backend/page/change.html"
    title = "修改密码"

    @method_decorator(xframe_options_exempt)
    def get(self, request):
        return render(request, self.template_name, {'title': self.title})

    @staticmethod
    def post(request):
        password0 = request.POST.get("old_password", "")
        password1 = request.POST.get("new_password", "")
        password2 = request.POST.get("again_password", "")

        if password1 != password2:
            data = {"status": 403, "msg": "两次密码不同"}
            return JsonResponse(data, safe=False)

        user = authenticate(username=request.user.username, password=password0)
        if user is not None and user.is_active:
            user.set_password(password1)
            user.save()
            data = {"status": 200, "msg": "密码修改成功"}
            return JsonResponse(data, safe=False)

        else:
            data = {"status": 403, "msg": "旧密码不匹配"}
            return JsonResponse(data, safe=False)


class RegView(View):

    @staticmethod
    def get(request):
        user_id = Users.objects.filter(username="luffy").first()
        print(user_id)
        if not user_id:
            Users.objects.create_user(username="luffy", password="shadow", is_superuser=True)

        return HttpResponse("shadow")
