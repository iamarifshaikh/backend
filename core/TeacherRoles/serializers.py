from rest_framework import serializers
from .models import *
from datetime import datetime
from django.utils import timezone

class TeacherRoleSerializer(serializers.Serializer):
    role_id = serializers.CharField(read_only=True)
    teacher_id = serializers.CharField(required=True)
    role_type = serializers.CharField(required=True)
    school_id = serializers.CharField(required=True)
    created_at = serializers.CharField(required=False)
    updated_at = serializers.CharField(required=False)
    subject_name = serializers.CharField(required=False)
    class_id =  serializers.CharField(required=False)

    def create(self,validated_data):
        return TeacherRoles.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.role_type = validated_data.get('role_type', instance.role_type)
        instance.subject_name = validated_data.get('subject_name', instance.subject_name)
        instance.class_id = validated_data.get('class_id', instance.class_id)
        instance.updated_at = datetime.now(timezone.now)
        instance.save()
        return instance
