from django.shortcuts import render

# Create your views here.
def filter(request):
    d={'data':'My name is balaji'}
    return render(request,'filter.html',d)