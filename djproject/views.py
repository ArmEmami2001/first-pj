from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render



def main(request):
    return render(request,'main.html')