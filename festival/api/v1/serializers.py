from rest_framework import serializers
from festival.models import Festival

class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival
        fields = [
            'id', 'title', 'slug', 'description', 'image',
            'start_date', 'end_date', 'location',
            'created_date', 'updated_date', 'is_active'
        ]
        read_only_fields = ['id', 'slug', 'created_date', 'updated_date']
