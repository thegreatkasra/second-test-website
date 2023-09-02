from django.urls import path    
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('login-email',views.login_view2,name='login-email'),
    path('logout',views.logout_view,name='logout'),
    path('signup',views.signup_view,name='signup'),
]