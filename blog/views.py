from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse


from .models import Post
# Create your views here.

# dummy data for now.



def starting_page(req):
    latest_posts=Post.objects.all().order_by('-event_date')[:3] 
    return render(req,'blog/index.html',{
        "posts":latest_posts,
    })
    
def posts(req):
    all_posts=Post.objects.all().order_by('-event_date')
    return render(req,'blog/all-posts.html',{
        "all_posts":all_posts
    })

def post_detail(req,slug):
    # idetified_post=  Post.objects.get(slug=slug) # no error handling  here
    idetified_post= get_object_or_404(Post,slug=slug)
    return render(req,"blog/post-detail.html",{
        "post":idetified_post,
        "post_tags":idetified_post.tags.all()
    })

