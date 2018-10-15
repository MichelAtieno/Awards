from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^upload/$', views.project, name='upload_project'),
    url(r'^review/(?P<project_id>\d+)',views.project_review ,name='project_review'),
    url(r'^accounts/edit', views.edit_profile, name='edit_profile'),
    url(r'^search/', views.search_profile, name='search'),
    url(r'^api/profile/$', views.ProfileList.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)