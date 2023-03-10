
from django.shortcuts import render
from home.forms import CustomerForm

def index(request):

    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form, 'hello':'PFE'}
    return render(request, 'home/index.html', context)
