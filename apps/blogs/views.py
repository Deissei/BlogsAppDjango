from django.shortcuts import render

from apps.blogs.models import Blog

def list_blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, "list.html", context)


def detail_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {
        "blog": blog
    }
    return render(request, "detail.html", context)
