from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
from healthmodels.models.HealthFacility import HealthFacility
from mtrack.models import Reporters
from api.serializers import HealthFacilitySerializer
from api.serializers import ReportersSerializer


class HealthFacilityViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing Health Facilities
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)
    #queryset = HealthFacility.objects.all()
    serializer_class = HealthFacilitySerializer

    def list(self, request, format=None):
        district = request.QUERY_PARAMS.get('district')
        district = district if district else ''
        if district:
            facilities = HealthFacility.objects.filter(district=district)
        else:
            facilities = HealthFacility.objects.all()
        serializer = HealthFacilitySerializer(facilities)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        facilities = HealthFacility.objects.filter(pk=pk)
        serializer = HealthFacilitySerializer(facilities)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

    @link()
    def district_facilities(self, request, pk=None):
        facilities = HealthFacility.objects.filter(district=pk)
        serializer = HealthFacilitySerializer(facilities)
        return Response(serializer.data)


class ReporterViewSet(viewsets.ModelViewSet):
    """
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)
    queryset = Reporters.objects.all()
    serializer_class = ReportersSerializer
