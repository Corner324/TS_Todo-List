from rest_framework import viewsets

from .serializers import TodoSerializer

from .models import Task


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
