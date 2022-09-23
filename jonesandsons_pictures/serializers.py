from rest_framework import serializers
from jonesandsons_pictures.models import Pictures

class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = (
            'PictureId',
            'PictureFileName',
        )