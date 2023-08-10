from django.shortcuts import render, HttpResponse

def home(requset):
    return render(requset,'index.html')
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# Create your views here.
