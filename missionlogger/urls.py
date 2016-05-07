from django.conf.urls import url
from django.views.generic import RedirectView
from .views import Index, MissionDetail, MissionCreate, MissionUpdate, MissionDelete, VesselCreate

app_name = 'missionlogger'
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='missions')),
    url(r'^missions$', Index.as_view(), name='index'),
    url(r'^missions/(?P<mission_status>\d)$', Index.as_view(), name='index-by-status'),
    url(r'^missions/(?P<vessel_name>.+)$', Index.as_view(), name='index-by-name'),
    url(r'^mission/(?P<mission_id>\d+)$', MissionDetail.as_view(), name='mission-detail'),
    url(r'^mission/add$', MissionCreate.as_view(), name='mission-add'),
    url(r'^mission/(?P<pk>\d+)/update$', MissionUpdate.as_view(), name='mission-update'),
    url(r'^mission/(?P<pk>\d+)/delete$', MissionDelete.as_view(), name='mission-delete'),
    url(r'^vessel/add$', VesselCreate.as_view(), name='vessel-add'),
]

