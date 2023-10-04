from django.urls import path
from apps.blogs.views import list_blogs, detail_blog

urlpatterns = [
    path('', list_blogs, name="list_blogs"),
    path('blogs/<int:pk>/', detail_blog, name="detail_blog"),
]
