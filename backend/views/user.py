from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt

from librarys.mixin.permission import LoginRequiredMixin

from backend.models.users import Users


class UserView(LoginRequiredMixin, ListView):
    template_name = "backend/page/user.html"

    @method_decorator(xframe_options_exempt)
    def get(self, request):
        return render(request, self.template_name)

    @staticmethod
    def post(request):
        uid = request.POST.get("id", "")
        user_id = uid.split(",")
        Users.objects.filter(id__in=user_id).delete()

        data = {"status": 200, "msg": "用户删除成功"}
        return JsonResponse(data, safe=False)


class AddUserView(LoginRequiredMixin, ListView):
    template_name = "backend/page/add.html"

    @method_decorator(xframe_options_exempt)
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(xframe_options_exempt)
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        super_user = request.POST.get("super")
        sex = request.POST.get("sex")
        rept_password = request.POST.get("rept_password")
        remark = request.POST.get("remark")

        if password != rept_password:
            data = {"status": 403, "msg": "两个密码不一致"}
            return JsonResponse(data, safe=False)

        if Users.objects.filter(username=username).count() != 0:
            data = {"status": 403, "msg": "用户已存在"}
            return JsonResponse(data, safe=False)

        try:
            super_user = int(super_user)

        except TypeError:
            data = {"status": 403, "msg": "参数类型错误"}
            return JsonResponse(data, safe=False)

        if sex == "1":
            sex = "男"
        elif sex == "0":
            sex = "女"

        Users.objects.create_user(username=username, password=password, is_superuser=super_user, sex=sex, remark=remark)

        data = {"status": 200, "msg": "用户创建成功"}
        return JsonResponse(data, safe=False)
