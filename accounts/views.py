from django.shortcuts import render

def login_view(request):
    if request.user.is_authenticated:
        msg = f'user authenticated as{request.user.username}'
    else:
        msg = 'user is not authenticated'
    return render(request,'accounts/login.html', {'msg':msg})


def logout_view(request):
    return render(request,'index.html')


def signup_view(request):
    return render(request,'accounts/signup.html')