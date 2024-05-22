from uuid import UUID

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import TextSerializer, NewTextSerializer, TextWithoutURLSSerializer
from urlModule import find_urls, delete_urls
from .services.text_service import TextService


class TextViewSet(ViewSet):
    text_service = TextService()

    def create(self, request):
        serializer = NewTextSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        text_instance = serializer.save()
        self.text_service.add_text(text_instance)
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request):
        texts = self.text_service.get_texts()
        return Response(TextSerializer(texts, many=True).data)

    def get_one(self, _, id: UUID):
        try:
            text = self.text_service.get_text_by_id(id)
            return Response(TextSerializer(text).data)
        except KeyError as e:
            raise NotFound(e)


    def find_urls(self, _, id: UUID):
        urls = find_urls(self.text_service.get_text_by_id(id).text)
        return Response({"urls": urls})


    def delete_urls(self, _, id: UUID):
        updated_text = delete_urls(self.text_service.get_text_by_id(id).text)
        serializer = TextWithoutURLSSerializer({'text': updated_text})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete_text(self, request, id: UUID):
        self.text_service.delete_text(id)
        return Response(status=status.HTTP_200_OK)
