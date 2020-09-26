from front.views.index import index

from django.urls import path

urlpatterns = [
    path('index/', index),
    #    path('admin/', admin.site.urls),
]
