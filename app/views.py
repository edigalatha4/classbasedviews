from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View,TemplateView
# Create your views here.
## Function Based View to handle the djangoforms

def fbv_djangoform(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))
    return render(request,'fbv_djangoform.html',d)

# CBV to handle the djangoforms

class cbvdjangoform(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'cbv_djangoform.html',d)
    
    def post(self,request):
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))



#FBV for returning string as response

def fbv_string(request):
    return HttpResponse('this is fbv_string')

class cbvstring(View):
    def get(self,request):
        return HttpResponse('this is cbv string')


#FBV to render html file and send context data

def fbv_htmlpage(request):
    d={'name':'JOSHI'}
    return render(request,'fbv_htmlpage.html',d)

#CBV to render htmlfile and send context data

class cbvhtmlpage(View):
    def get(self,request):
        d={'name':'Joshi'}
        return render(request,'cbv_htmlpage.html',d)


