from django.contrib import admin
from django.urls import include, path ,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap 
from robots.views import RuleList
from django.contrib.auth import views as auth_views
from . import views                #coming soon page

sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = [        
    #path('', views.splash_page, name='splash_page'),              #coming soon page
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('blog/',include('blog.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  #Sitemap
    path("robots.txt", RuleList.as_view(), name="robots"), #robot SEO url
    path('summernote/', include('django_summernote.urls')), #summernote config url
    path('captcha/', include('captcha.urls')), #captcha config url
    path('accounts/', include('accounts.urls')), #Accounts App url
    #Password_reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
           
]

#404 handler
handler404 = 'website.views.custom_404'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)