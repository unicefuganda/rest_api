from healthmodels.models.HealthFacility import HealthFacility
#from healthmodels.models.HealthProvider import HealthProvider
from mtrack.models import Reporters
from rest_framework import serializers


class HealthFacilitySerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.Field(source='type.name')
    is_hmis033b = serializers.Field(source='is_hmis033b')
    catchment_areas = serializers.SerializerMethodField('get_catchment_areas')

    class Meta:
        model = HealthFacility
        fields = (
            'id', 'name', 'level', 'owner', 'uuid', 'district',
            'authority', 'last_reporting_date', 'active', 'is_hmis033b',
            'catchment_areas'
        )

    def get_catchment_areas(self, obj):
        return obj.catchment_areas.all().values('name', 'type')


class ReportersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reporters
        fields = (
            'id', 'name', 'groups', 'connections', 'district',
            'facility', 'active'
        )
