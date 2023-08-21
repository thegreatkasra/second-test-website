from django.http import HttpResponseRedirect
from django.shortcuts import render
from website.forms import ContactForm , NewsletterForm

def index(request):
    return render(request,'index.html')

#Form of contact us!!
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()    
    form = ContactForm()
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def element(request):
    return render(request,'element.html')

#Form of Newsletter!! after Enter Ur email we save it and return you back to home.html !!
def Newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
