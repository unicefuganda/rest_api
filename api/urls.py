#from django.conf.urls import patterns, url, include
from django.conf.urls.defaults import patterns, url, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
#router.register(r'snippets', views.SnippetViewSet)
router.register(r'healthfacilities', views.HealthFacilityViewSet, 'facilities')
router.register(r'reporters', views.ReporterViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    #url(r''),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
