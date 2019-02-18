#coding=utf8
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Subversion
import forms
import models
import django.utils.timezone as timezone
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.decorators import permission_required
import paramiko

def SSH(host,username,password,svnname,filename):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=22, username=username, password=password)
    #command = 'cd /var/tmp/svn && svnadmin create %s && cp LMK/hooks/pre-commit %s/hooks/ && chmod -R 777 %s' %(svnname,svnname,svnname)
    command = 'cd /data/svn/ && sh /data/svn/svn_create.sh %s /var/tmp/svnupload/%s' %(svnname,filename)
    print command
    stdin, stdout, stderr = ssh.exec_command(command)
    ssh.close()




def svnlist(request):
	svn_list = Subversion.objects.all()
	return render(request, 'svn/svn_list.html',context ={ 'svn_list': svn_list})


def svn_add(request):
    if request.method == "POST":
            print "bbb"
            form = forms.SvnInfo(request.POST,request.FILES)
            #message = "请检查填写的内容！"
            if form.is_valid():

                svn_enname = form.cleaned_data['svn_enname']
                svn_company = form.cleaned_data['svn_company']
                svn_zhname = form.cleaned_data['svn_zhname']
                svn_url = form.cleaned_data['svn_url']
                print "start"
                print svn_enname,svn_company,svn_url,svn_zhname

                try:
                    File = request.FILES.get("myfile", None)
                    print File.name
                    if File:
                        with open("./svnupload/%s" % File.name, 'wb+') as f:
                            # 分块写入文件
                            for chunk in File.chunks():
                                f.write(chunk)
                    else:
                        print "no file"


                    print svn_enname, svn_company, svn_url, svn_zhname
                    SSH(host="192.168.11.1",username="root",password="123456",svnname=svn_enname,filename=File.name)
                    new = models.Subversion.objects.create()
                    new.svn_enname = svn_enname
                    new.svn_company = svn_company
                    new.svn_zhname = svn_zhname
                    new.svn_url = svn_url
                    new.save()
                    return redirect('svnlist.html')
                except:
                    message = ""
                    return redirect('svn_add.html')
            else:
                print "aaaa"
                print form.errors

    form = forms.SvnInfo()
    return render(request, 'svn/svn_add.html', {'form': form})

def svn_delete(request,pk):
    svn=Subversion.objects.get(pk=pk)
    svn.delete()
    return redirect('/svnlist')