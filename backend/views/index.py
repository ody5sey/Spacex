from django.shortcuts import render, HttpResponse
from django.views.generic import View

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


class RegView(View):

    @staticmethod
    def get(request):
        user_id = Users.objects.filter(username="luffy").first()
        print(user_id)
        if not user_id:
            Users.objects.create_user(username="luffy", password="shadow", is_superuser=True)

        return HttpResponse("shadow")
