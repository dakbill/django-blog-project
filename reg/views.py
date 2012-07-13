"""
Code that should be copy and pasted in to
reg/views.py to as a skeleton for creating
the authentication views
"""
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def do_login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        passw=request.POST['password']
        print str(uname)
        print str(passw)
        user=authenticate(username=uname,password=passw)
        if user is not None:
        	if user.is_active:
        		print 'Correct username and password'
        	else:
        		print 'Account disabled'
        else:
        	print 'Incorrect password'            
    form = LoginForm()
    return render_to_response('reg/login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated()
    })

@csrf_exempt
def do_logout(request):
    logout(request)
    return render_to_response('reg/logout.html')
