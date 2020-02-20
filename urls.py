from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    url(r'^albums/$', views.AlbumList.as_view(), name='album-list'),
    url(r'^bands/$', views.BandList.as_view(), name='band-list'),
    url(r'^members/$', views.MemberList.as_view(), name='member-list'),

    url(r'^music/(?P<pk>[0-9]+)/$', views.MusicDetail.as_view(), name='music-detail'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name='album-detail'),
    url(r'^band/(?P<pk>[0-9]+)/$', views.BandDetail.as_view(), name='band-detail'),
    url(r'^member/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view(), name='member-detail'),
]