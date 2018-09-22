from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from dbapp import views as dbapp
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dbapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    ################### DASHBOARD URLS ###############

    url(r'^admin/', admin.site.urls),
    url(r'^$', dbapp.index, name='home'),
    url(r'^orders$', dbapp.index, name='home'),
    url(r'^order/(?P<order_id>\d+)/$', dbapp.show, name='show'),
    url(r'^order/new/$', dbapp.new, name='new'),
    url(r'^order/edit/(?P<order_id>\d+)/$', dbapp.edit, name='edit'),
    url(r'^order/delete/(?P<order_id>\d+)/$', dbapp.destroy, name='delete'),
    url(r'^users/login/$', auth.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^users/logout/$', auth.LogoutView.as_view, {'next_page': '/login'}, name='logout'),
]
