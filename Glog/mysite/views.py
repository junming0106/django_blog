from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime
# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return (render(request, "index.html", locals())) # 會將作用域的變數以字典回傳 posts/now

def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug) # 將網址得到的slug(後) -> slug(前)
        print(post)
        if post != None:
            return render(request, "post.html", locals())
    except:
        return redirect('/')