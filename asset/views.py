#coding=utf8
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Asset
import forms
from .forms import Assetadd
import models

def index(request):
	return render(request, 'index.html')
def asset_list(request):
	asset_list = Asset.objects.all()
	return render(request, 'tables.html',context ={ 'asset_list': asset_list})

def asset_l(request):
	asset_list = Asset.objects.all()
	return render(request, 'asset/asset_list.html',context ={ 'asset_list': asset_list})

def flot(request):
	return render(request, 'flot.html')

def morris(request):
	return render(request, 'morris.html')

def asset_add(request):
	if request.method == "POST":
		form = forms.Assetadd(request.POST)
        	message = "请检查填写的内容！"
        	if form.is_valid():
            		asset_name = form.cleaned_data['asset_name']
            		asset_number = form.cleaned_data['asset_number']
            		asset_source = form.cleaned_data['asset_source']
            		asset_people = form.cleaned_data['asset_people']
            		asset_application = form.cleaned_data['asset_application']			
            		try:
				print asset_name,asset_number,asset_source,asset_people,asset_application
                		new = models.Asset.objects.create()
				new.asset_name = asset_name
				new.asset_number = asset_number
				new.asset_source = asset_source
				new.asset_people = asset_people
				new.asset_application = asset_application
				new.save()
				return redirect('asset_list.html')
            		except:
                		message = "填写错误！"
				return redirect('asset/asset_add.html')

   	form = forms.Assetadd()
        return render(request, 'asset/asset_add.html', {'form' : form })

def asset_mod(request,pk):
        asset = Asset.objects.get(pk=pk)
#	print asset.asset_application
	if request.method == "POST":
                form = forms.Assetadd(request.POST,initial = [{'asset_name': asset.asset_name,'asset_number': asset.asset_number,'asset_source':asset.asset_source,'asset_people':asset.asset_people,'asset_application':asset.asset_application}])

                if form.is_valid():

			asset_name = form.cleaned_data['asset_name']
                        asset_number = form.cleaned_data['asset_number']
                        asset_source = form.cleaned_data['asset_source']
                        asset_people = form.cleaned_data['asset_people']
                        asset_application = form.cleaned_data['asset_application']

			asset.asset_name = asset_name
                        asset.asset_number = asset_number
                        asset.asset_source = asset_source
                        asset.asset_people = asset_people
                       	asset.asset_application = asset_application
                        asset.save()
			return redirect('/asset_list')
#			return render(request, 'asset/asset_mod.html', {'form' : form ,'asset_name':asset.asset_name})
	
	form = forms.Assetadd(initial={
			'asset_name': asset.asset_name,
			'asset_number': asset.asset_number,
			'asset_source':asset.asset_source,
			'asset_people':asset.asset_people,
			'asset_application':asset.asset_application
					})
	return render(request, 'asset/asset_mod.html', {'form' : form })

def asset_delete(request,pk):
	asset=Asset.objects.get(pk=pk)
	asset.delete()
	return redirect('/asset_list')
