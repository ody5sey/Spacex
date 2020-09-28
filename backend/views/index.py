from django.shortcuts import render
from django.views.generic import View

from librarys.mixin.permission import LoginRequiredMixin
from backend.models.users import AdminUser


class IndexView(LoginRequiredMixin, View):
    index_templates = "backend/index.html"
    title = "管理"

    def get(self, request):
        user_id = AdminUser.objects.filter(username="luffy").first()
        if not user_id:
            AdminUser.objects.create_user(username="luffy", password="shadow", is_superuser=True)

        return render(request, self.index_templates, {'title': self.title})
