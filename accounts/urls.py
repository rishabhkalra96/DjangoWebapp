from django.conf.urls import url
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
from . import views


urlpatterns = [
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile, name='view_profile_with_primary_key'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset,
        {
            'template_name': 'accounts/reset_password.html',
            'post_reset_redirect': 'accounts:password_reset_done',
            'email_template_name': 'accounts/reset_password_email.html'
        }, name='password_reset'),

    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'},
        name='password_reset_done'),

    url(r'^reset-password/confirm/$', password_reset_confirm, name='password_reset_confirm'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {
            'template_name': 'accounts/reset_password_confirm.html',
            'post_reset_redirect': 'accounts:password_reset_complete'
        }, name='password_reset_confirm'),

    url(r'^password-reset/complete/$', password_reset_complete,
        {
            'template_name': 'accounts/reset_password_complete.html'
        }, name='password_reset_complete')
]
