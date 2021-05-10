from django.conf.urls import url, include
from artist.view_api import ArtistViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers,routers
artist_list = ArtistViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
artist_detail = ArtistViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^artist/$',
        artist_list,
        name='artist-list'),
    url(r'^custom/artist/$',
        ArtistViewSet.custom_list,
        name='custom-artist-list'),
    url(r'^custom/artist/create$',
        ArtistViewSet.custom_create,
        name='custom-artist-create'),
    url(r'^artist/(?P<pk>[0-9]+)/$',
        artist_detail,
        name='artist-detail'),
])