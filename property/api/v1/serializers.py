from rest_framework import serializers

from property.models import Property, Reservation

from useraccount.api.v1.serializers import UserDetailSerializer


class PropertiesListSerializer(serializers.ModelSerializer):
    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'price_per_night',
            'image_urls',
        )

    def get_image_urls(self, obj):
        return obj.get_image_urls()



class PropertiesDetailSerializer(serializers.ModelSerializer):
    landlord = UserDetailSerializer(read_only=True)
    image_urls = serializers.SerializerMethodField()


    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'description',
            'price_per_night',
            'image_urls',
            'bedrooms',
            'buildingsmeter',
            'floorareameters',
            'guests',
            'landlord',
        )

    def get_image_urls(self, obj):
        return obj.get_image_urls()
    


    


class ReservationsListSerializer(serializers.ModelSerializer):
    property = PropertiesListSerializer(read_only=True, many=False)

    class Meta:
        model = Reservation
        fields = (
            'id', 'start_date', 'end_date', 'number_of_nights', 'total_price', 'property'
        )

