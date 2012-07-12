"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Post, Comment 
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def post_list(request):
	posts = Post.objects.all()
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts':posts })
	return HttpResponse(t.render(c))
class CommentForm(ModelForm):
	class Meta:
		model=Comment
		exclude=['post']
@csrf_exempt
def post_detail(request, id, showComments=False):
		wanted_post=Post.objects.get(pk=id)
		if request.method == 'POST':
			comment=Comment(post=wanted_post)	
			form = CommentForm(request.POST,instance=comment)
			if form.is_valid():
				form.save()
			else:
				print 'invalid'
			return HttpResponseRedirect(request.path)
		else:
			form = CommentForm()
		comments=Comment.objects.filter(post=wanted_post)
		t = loader.get_template('blog/post_detail.html')
		c = Context({'comments':comments,'form':form,'wanted_post':wanted_post })
		return HttpResponse(t.render(c))
def post_search(request, term):
    pass

def home(request):
    return render_to_response('blog/base.html',{})

