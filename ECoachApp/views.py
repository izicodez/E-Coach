from django.shortcuts import render, HttpResponse, redirect
from ECoachApp.models import List
from ECoachApp.forms import ListForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(request, 'index.html', {'all_items':all_items})
        else:
            all_items = List.objects.all
            return render(request, 'index.html',{'all_items':all_items})

    else:
        all_items = List.objects.all
        return render(request, 'index.html', {'all_items':all_items})
    # context = {
    #     'var1':'21.00',
    #     'var2':'40.00'
    # }
    # return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')     

def contact(request):
    return render(request, 'contact.html')    

def base(request):
    return render(request, 'base.html') 

def delete(request, list_id):
    #List gives a dictionary
    item= List.objects.get(pk=list_id)
    item.delete()
    
    return redirect('home')

def start(request, list_id):
    #List gives a dictionary
    item= List.objects.get(pk=list_id)
    name = item.item # This will give me the name
    
    return render(request,'start.html', {'item':item})


def timer(request,list_id):
    if request.method == 'POST':
        item= List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)


        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('home')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'timer.html', {'item':item})
    
    # context = {
    #     'var1':'21.00',
    #     'var2':'40.00'
    # }
    # return render(request, 'index.html', context)