from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^profile/$',views.profile,name= 'profile'),
    url('^$', views.all_images, name='allImages'),

]