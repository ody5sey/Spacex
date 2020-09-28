from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt

from librarys.mixin.permission import LoginRequiredMixin
from backend.models.users import AdminUser


class MenuView(LoginRequiredMixin, View):
    index_templates = "backend/page/menu.html"

    @method_decorator(xframe_options_exempt)
    def get(self, request):
        return render(request, self.index_templates)
