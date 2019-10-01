from django.shortcuts import render

# Create your views here.
def page1(request):
    return render(request,'sample1.html')

def page2(request):
    return render(request,'sample2.html')
    
def page3(request):
    return render(request,'sample3.html')
    