#from django.forms import widgets
from rest_framework import serializers
from rwfm.models import Object
from rwfm.models import Subject


class SubjectSerializer(serializers.Serializer):
    sub_id = serializers.CharField()
    admin = serializers.CharField()
    readers = serializers.CharField()
    writers = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Subject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.sub_id = validated_data.get('sub_id', instance.sub_id)
        instance.admin = validated_data.get('admin', instance.admin)
        instance.readers = validated_data.get('readers', instance.readers)
        instance.writers = validated_data.get('writers', instance.writers)

        instance.save()
        return instance

class ObjectSerializer(serializers.Serializer):
    obj_id = serializers.CharField()
    admin = serializers.CharField()
    readers = serializers.CharField()
    writers = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Object.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.obj_id = validated_data.get('obj_id', instance.obj_id)
        instance.admin = validated_data.get('admin', instance.admin)
        instance.readers = validated_data.get('readers', instance.readers)
        instance.writers = validated_data.get('writers', instance.writers)

        instance.save()
        return instance

