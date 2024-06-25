"""
URL configuration for proiect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from myApp.views import home_screen_view

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
)

from accommodation.views import (
    upload_accommodation_view,
    upload_accommodation_success_view,
    accommodation_detail_view,
    reservation_success_view,
    reservation_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name = 'home'),
    path('register/', registration_view, name = 'register'),
    path('logout/', logout_view, name = 'logout'),
    path('login/', login_view, name = 'login'),
    path('account/', account_view, name = 'account'),
    
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

    path('upload-accommodation/', upload_accommodation_view, name='upload_accommodation'),
    path('upload-accommodation-success/', upload_accommodation_success_view, name='upload_accommodation_success'),
    #path('accommodation_detail/', accommodation_detail_view, name='accommodation_detail'),
    path('<int:accommodation_id>/', accommodation_detail_view, name='accommodation_detail_id'),
    path('accommodation/<int:accommodation_id>/reserve/', reservation_view, name='reserve_accommodation'),
    path('reservation/success/', reservation_success_view, name='reservation_success'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)