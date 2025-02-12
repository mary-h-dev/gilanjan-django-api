from django.forms import ModelForm

from property.models import Property


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = (
            'title',
            'description',
            'price_per_night',
            'bedrooms',
            # 'bathrooms',
            'buildingsmeter',
            'floorareameters',
            'guests',
            'country',
            'country_code',
            'category',
            'image',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'image6',
            'image7',
            'image8',
            'image9',
        )