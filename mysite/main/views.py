from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    about = About.objects.all().first()
    class_first = Class.objects.all().first()
    class_block = Class.objects.all()
    blog_first = Blog.objects.all().first()
    block_image = Blog.objects.all()
    main = Main.objects.all().first()
    return render(request, 'main/index.html', context={
        'about': about,
        'class_first': class_first,
        'class_block': class_block,
        'blog_first': blog_first,
        'blog_image': block_image,
        'main': main
    })


def about(request):
    about = About.objects.all().first()
    return render(request, 'main/about.html', context={
        'about': about
    })

def clas(request):
    class_first = Class.objects.all().first()
    class_block = Class.objects.all()
    return render(request, 'main/class.html', context={
        'class_first': class_first,
        'class_block': class_block
    })


def blog(request):
    blog_first = Blog.objects.all().first()
    block_image = Blog.objects.all()
    return render(request, 'main/blog.html', context={
        'blog_first': blog_first,
        'block_image': block_image
    })