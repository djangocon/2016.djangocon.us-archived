from django.shortcuts import render

from pinax.blog.models import Post

def homepage(request):
    return render(request, "homepage.html", {
        'latestposts': Post.objects.published().order_by("published")[:10]})