from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
       return render(request,'website/index.html')

def analyze(request):
       context=None
       if request.method=='GET':
              textname=request.GET.get('textname')
              removep=request.GET.get('removep')
              puchtuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
              analyze=""
              if removep=='on':
                for chr in textname:
                        if chr not in puchtuation:
                                analyze+=chr
                context={
                       'data':analyze
                }
                
            
       return render(request,'website/analyze.html',context)