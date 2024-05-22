from .models import Text
from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField()
    text = serializers.CharField()


class NewTextSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField()
    text = serializers.CharField()

    def create(self, validated_data):
        id = validated_data.get('id')
        if id is not None:
            return Text(validated_data['name'], validated_data['text'], id)
        else:
            return Text(validated_data['name'], validated_data['text'])


class URLSerializer(serializers.Serializer):
    urls = serializers.ListField(child=serializers.URLField())


class TextWithoutURLSSerializer(serializers.Serializer):
    text = serializers.CharField()
