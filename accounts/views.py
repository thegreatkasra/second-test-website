from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.forms import AuthenticationForm            #login
from django.contrib.auth.decorators import login_required           # @login_required decorator !
from accounts.forms import CustomUserCreationForm                   #Signup


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                if username and password:
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/')
                    else:
                        # Handle authentication failure
                        return render(request, 'accounts/login.html', {'error_message': 'Invalid username or password'})
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)  # Use the custom form
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = CustomUserCreationForm()  # Use the custom form
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')












