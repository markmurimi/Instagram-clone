from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^profile/$',views.profile,name= 'profile'),
    url(r'^allImages/$', views.all_images, name='allImages'),
    url(r'^accounts/', include('registration.backends.simple.urls','allImages')),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^allImages/search/', views.search, name='search'),
    url(r'^details/(?P<photo_id>[0-9]+)/$', views.image_details, name='image_details'),
    url(r'^follow/(\d{1})/$',views.follow,name="follow"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)