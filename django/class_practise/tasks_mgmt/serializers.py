from rest_framework import serializers
from typing import override
from .models import Task, User
from .utils import BcryptPasswordUtil


def _validate_bcrypt_password_length(password):
    if len(password.encode("utf-8")) > 72:
        raise serializers.ValidationError(
            "Password must be at most 72 bytes when encoded as UTF-8."
        )
    return password

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

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id","username","email","first_name","last_name","password","created_at","updated_at","is_active"]
        read_only_fields = ["id","created_at","update_at"]
    def validate_password(self, password):
        return _validate_bcrypt_password_length(password)

    def create(self, validated_data):
        # validated_data["password"] = BcryptPasswordUtil.hash_password(
        #     validated_data["password"]
        # )
        # return super().create(validated_data)
        password = self.validate_password.pop("password")
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user


    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        instance = super().update(instance, validated_data)
        if password is not None:
            # instance.password = BcryptPasswordUtil.hash_password(password)
            # instance.save(update_fields=["password"])
            instance.set_password(password)
            instance.save(update_fields=["password"])
        return instance

class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        depth = 1

class AllTaskUserSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    task_list = TaskSerializer(many=True, read_only=True)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_password(self, password):
        return _validate_bcrypt_password_length(password)