from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.forms import AuthenticationForm

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



def logout_view(request):
    return render(request,'index.html')


def signup_view(request):
    return render(request,'accounts/signup.html')