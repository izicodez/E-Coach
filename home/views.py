from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'var1':'20.00',
        'var2':'40.00'
    }
    return render(request, 'index.html', context)
    #return HttpResponse("THis is home page")

def about(request):
    return render(request, 'about.html')     

def contact(request):
    return HttpResponse("THis is contact page")    

def base(request):
    return render(request, 'base.html') 
