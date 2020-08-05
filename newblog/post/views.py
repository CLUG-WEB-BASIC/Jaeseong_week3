from django.shortcuts import render

def read_blog_list(request):
    return render(request, 'post/blog_list.html')