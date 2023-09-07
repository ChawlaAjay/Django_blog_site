from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

# dummy data for now.

all_posts=[
    {
        "slug": "Hike-in-the-mountains",
        "image": "mountains.jpg",
        "author":"ajay",
        "date":date(2023,9,4),
        "title":"Mountains-Hiking",
        "excerpt": "here's nothing like the views you get when hiking in the mountains!\
        And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                    aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                    velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
                    """,
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Ajay",
        "date": date(2021, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Ajay",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]
# def get_date(post):
#     return post['date']

def starting_page(req):
    sorted_posts=sorted(all_posts,key=lambda p:p['date'])
    latest_posts=sorted_posts[-3:]
    return render(req,'blog/index.html',{
        "posts":latest_posts,
    })
    
def posts(req):
    return render(req,'blog/all-posts.html',{
        "all_posts":all_posts
    })

def post_detail(req,slug):
    idetified_post=next(post for post in all_posts if post['slug']==slug)
    return render(req,"blog/post-detail.html",{
        "post":idetified_post,
    })