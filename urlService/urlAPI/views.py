from uuid import UUID

from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import TextSerializer, NewTextSerializer, TextWithoutURLSSerializer
from urlModule import find_urls, delete_urls
from .services.text_service import TextService


class TextViewSet(ViewSet):
    text_service = TextService()

    def create(self, request):
        serializer = NewTextSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            text_instance = serializer.save()
            self.text_service.add_text(text_instance)
            return Response(TextSerializer(text_instance).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        texts = self.text_service.get_texts()
        return Response(TextSerializer(texts, many=True).data, status=status.HTTP_200_OK)

    def get_one(self, request, id: UUID):
        try:
            text = self.text_service.get_text_by_id(id)
            return Response(TextSerializer(text).data, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"detail": "Text not found."}, status=status.HTTP_404_NOT_FOUND)

    def find_urls(self, request, id: UUID):
        try:
            text = self.text_service.get_text_by_id(id)
            urls = find_urls(text.text)
            return Response({"urls": urls}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"detail": "Text not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete_urls(self, request, id: UUID):
        try:
            text = self.text_service.get_text_by_id(id)
            updated_text = delete_urls(text.text)
            text.text = updated_text
            serializer = TextWithoutURLSSerializer(text)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"detail": "Text not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete_text(self, request, id: UUID):
        try:
            self.text_service.delete_text(id)
            return Response({"detail": "Text deleted successfully."}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"detail": "Text not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
