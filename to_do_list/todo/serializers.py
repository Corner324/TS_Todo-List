from .models import Task, Tag
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)


    class Meta:
        model = Task
        fields = "__all__"