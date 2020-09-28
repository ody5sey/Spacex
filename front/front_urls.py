from front.views.index import LoginView

from django.urls import path

urlpatterns = [
    path('', LoginView.as_view()),
]
