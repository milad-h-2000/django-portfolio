from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    all_blogs = Blog.objects.all()
    return render(request, 'blog\\all_blogs.html', {'all_blogs': all_blogs})

def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog\\details.html', {'blog': blog})