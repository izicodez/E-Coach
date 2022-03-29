from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'var1':'20.00',
        'var2':'40.00'
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')     

def contact(request):
    return render(request, 'contact.html')    

def base(request):
    return render(request, 'base.html') 
