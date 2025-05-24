from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
       return render(request,'website/index.html')

def analyze(request):
       context=None
       if request.method=='GET':
              textname=request.GET.get('textname')
              convert=request.GET.get('convert')
              puchtuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
              analyze=""
              if convert=='remove':
                for chr in textname:
                        if chr not in puchtuation:
                                analyze+=chr
                data={'data':analyze}
              elif convert=='convertU':
                     for chr in textname:
                        if chr not in puchtuation:
                                analyze+=chr
                     value=analyze.upper()
                     data={ "data":value}
              elif convert=='convertL':
                     for chr in textname:
                        if chr not in puchtuation:
                                analyze+=chr
                     value=analyze.lower()
                     data={ "data":value}
              else:
                     return HttpResponse("Please Input Some Data")
              return render(request,'website/analyze.html',data)