from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.forms import AuthenticationForm            #login
from django.contrib.auth.decorators import login_required           # @login_required decorator !
from accounts.forms import UserCreationForm                         #Signup
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django import forms


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                if username and password:
                    user = authenticate(request, username=username , password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/')
                    else:
                        # Handle authentication failure
                        return render(request, 'accounts/login.html', {'error_message': 'Invalid username or password'})
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'registration/login.html', context)
    
def login_view2(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                email = request.POST.get('email')
                password = request.POST.get('password')
                if email and password:
                    user = authenticate(request, email=email, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/')
                    else:
                        # Handle authentication failure
                        return render(request, 'accounts/login-email.html', {'error_message': 'Invalid username or password'})
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'registration/login-email.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


#Signup_Form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('/') 
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


#password_reset
class CustomPasswordResetView(PasswordResetView):
    template_name = 'password-reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')





