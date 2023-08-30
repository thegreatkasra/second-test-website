from django.http import HttpResponseRedirect
from django.shortcuts import render 
from website.forms import ContactForm , NewsletterForm 
from django.contrib import messages

def index(request):
    return render(request,'index.html')


#Form of contact us!!
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)  # Create instance without saving to DB
            contact_instance.name = 'unknown'  # Change the name to "unknown"
            contact_instance.save()  # Now save to the DB
            messages.add_message(request , messages.SUCCESS, 'Successfull !') #success message
            #return JsonResponse({'success': True})
        else:           
            messages.add_message(request,messages.ERROR, 'ERROR! Try again carefully!') #error message
            #return JsonResponse({'success': False})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form} )



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

