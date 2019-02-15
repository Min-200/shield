#coding=utf8
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Subversion
#import forms
import models
import django.utils.timezone as timezone
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.decorators import permission_required

def svnlist(request):
	svn_list = Subversion.objects.all()
	return render(request, 'svn/svn_list.html',context ={ 'svn_list': svn_list})