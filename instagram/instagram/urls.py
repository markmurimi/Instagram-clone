from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('insta.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^tinymce/', include('tinymce.urls')),

]
