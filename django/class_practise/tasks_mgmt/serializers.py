from rest_framework import serializers
from typing import override
from .models import Task
# class TaskSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     completed = serializers.BooleanField(default=False)
#     updated_at = serializers.DateTimeField(read_only=True)
    
#     @override
#     def create(self, validated_data):
#         return Task.objects.create(**validated_data)
    
#     @override
#     def update(self,instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.completed = validated_data.get('completed', instance.completed)
#         instance.save()
#         return instance

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"