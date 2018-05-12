from django.conf.urls import url,include
from . import views

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^welcome/$',views.welcome,name = 'welcome'),
    url(r'^profile/$',views.profile,name= 'profile'),
    url(r'^allImages/$', views.all_images, name='allImages'),
    url(r'^accounts/', include('registration.backends.simple.urls','allImages')),
    url(r'^new/post$', views.new_post, name='new-post')

]