from rest_framework import viewsets, filters

from .serializers import TagSerializer, TodoSerializer

from .models import Tag, Task

from django_filters.rest_framework import DjangoFilterBackend


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["is_completed", "tags__name"]
    ordering_fields = ["due_date", "created_at", "title"]
    ordering = ["-created_at"]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
