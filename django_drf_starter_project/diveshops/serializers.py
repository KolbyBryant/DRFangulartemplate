from rest_framework import serializers
from diveshops.models import Store

class StoreSerializer(serializers.ModelSerializer):
    """ REPRESENTS STORE MODEL"""
    class Meta:
        model = Store
        fields = (
            "name", "description", "location", "number", "address", "opening_date", "website"
        )
