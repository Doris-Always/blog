import datetime

from django.shortcuts import render, get_object_or_404
from my_blog_app.models import Post


# Create your views here.
#
# my_posts = [
#     {
#         "id": 1,
#         "title": "Html i an nutshell",
#         "content": "Needed feebly dining oh talked wisdom oppose at."
#                    "Applauded use attempted strangers now are middleton concluded had"
#                    "It is tried ﻿no added purse shall no on truth. Pleased anxious "
#                    "or as in by viewing forbade minutes prevent. Too leave had those get being led weeks"
#                    " blind. Had men rose from down lady able. Its son him ferrars proceed six parlors."
#                    " Her say projection age announcing decisively men. Few gay sir those",
#         "date": datetime.datetime.now(),
#         "author": "Mr Anjola"
#     },
#     {
#         "id": 2,
#         "title": "possibilities of acceptance",
#         "content": "Oh acceptance apartments up sympathize astonished delightful. "
#                    "Waiting him new lasting towards. Continuing melancholy especially so to."
#                    " Me unpleasing impossible in attachment announcing so astonished."
#                    "What ask leaf may nor upon door. Tended remain my do stairs"
#                    "Oh smiling amiable am so visited cordial in offices hearted.",
#         "date": datetime.datetime.now(),
#         "author": "Mr Bennis"
#     },
#     {
#         "id": 3,
#         "title": "When life takes a break",
#         "content": "Waiting him new lasting enable. Continuing melancholy especially so to."
#                    " Me taking care impossible in attachment announcing so astonished."
#                    "What ask leaf may nor upon door. Tended remain my do stairs"
#                    "Oh smiling amiable am so visited in offices hearted.",
#
#         "date": datetime.datetime.now(),
#         "author": "Mr Kelechi"
#     }
# ]
#

def index(request):
    my_posts = Post.objects.all()
    return render(request, "my_blog_app/index.html", context={"my_posts": my_posts})


def post_page(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    return render(request, 'my_blog_app/post.html', {'post': posts})
    # post = my_posts[post_id - 1]
    # return render(request, "my_blog_app/post.html")
