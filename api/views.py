from rest_framework import viewsets
from .serializers import ApiSerializers
from .models import Api


class ApiViewSet(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializers
