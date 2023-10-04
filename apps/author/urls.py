from django.urls import path
from apps.author.views import list_blogs

urlpatterns = [
    path('', list_blogs, name="list_blogs"),
]
