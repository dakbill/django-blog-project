"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Post, Comment 


def post_list(request):
	posts = Post.objects.all()
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts':posts })
	return HttpResponse(t.render(c))


def post_detail(request, id, showComments=False):
	comments=Comment.objects.filter(pk=id)
	t = loader.get_template('blog/post_detail.html')
	c = Context({'comments':comments })
	return HttpResponse(t.render(c))
def post_search(request, term):
    pass

def home(request):
    return render_to_response('blog/base.html',{})

