from django.shortcuts import render
from.models import Post
# from django.http import HttpResponse
# Create your views here.
# posts=[
#     {
#         'author':'Samir Koirala',
#         'title':'Blog Post 1',
#         'content':'First post content',
#         'date_posted':'Aug 17 2024'
#     },
#         {
#         'author':'Pradip Chapagain',
#         'title':'Blog Post 2',
#         'content':'Second post content',
#         'date_posted':'Aug 19 2024'
#     }
# ]

def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})