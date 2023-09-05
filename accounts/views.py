from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.forms import AuthenticationForm            #login
from django.contrib.auth.decorators import login_required           #logout (@login_required decorator !)
from django.contrib.auth.forms import UserCreationForm              #Signup
from django import forms                                            #Signup
from django.contrib.auth.models import User                         #Signup
from django.contrib.auth.views import PasswordResetView             #passwordreset
from django.urls import reverse_lazy                                #passwordreset
from django.contrib import messages                                 #message




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username, email, or password. Please try again.')
        else:
            messages.error(request, 'Invalid username, email, or password. Please try again.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})
    



@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


#Signup_Form-username-email-pass
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()
    
    return render(request, 'registration/signup.html', {'form': form})



#Forget_password

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'                    #filename
    email_template_name = 'password_reset_email.html'        #filename
    subject_template_name = 'password_reset_subject.txt'     #filename
    success_url = reverse_lazy('password_reset_done')





