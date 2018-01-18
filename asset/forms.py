#coding=utf-8
from django import forms
class Assetadd(forms.Form):
    asset_name   = forms.CharField(label="设备名称", max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    asset_number = forms.CharField(label="设备编号", max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    asset_source = forms.CharField(label="设备来源", max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    asset_people = forms.CharField(label="使用人员", max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    asset_application =  forms.CharField(label="设备用途", max_length=500,widget=forms.TextInput(attrs={'class':'form-control'}))
