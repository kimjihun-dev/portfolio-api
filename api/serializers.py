from rest_framework import serializers
from .models import Api


class ApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = (
            'id', 'title', 'slug', 'content', 'skills', 'position', 'thumbnail', 'contentImg', 'site_view', 'code_view')
