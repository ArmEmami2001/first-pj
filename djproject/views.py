from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render



def main(request):
    return render(request,'main.html')

def first_pg(request):
    return render(request,'first_page.html')