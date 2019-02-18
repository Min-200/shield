#coding=utf-8
from django import forms
class SvnInfo(forms.Form):
    svn_enname = forms.CharField(label="仓库名", max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    svn_company = forms.CharField(label="公司", max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    svn_zhname = forms.CharField(label="英文名", max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    svn_url =  forms.CharField(label="SVN地址", max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
