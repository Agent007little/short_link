from rest_framework.generics import ListCreateAPIView
from .serializers import LinksUserSerializer
from links.models import ShortLink
from rest_framework.viewsets import ModelViewSet


# получение списка ссылок конкретного пользователя.
class LinksUser(ModelViewSet):
    queryset = ShortLink.objects.all()
    serializer_class = LinksUserSerializer

    def get_queryset(self):
        user = self.request.user
        return ShortLink.objects.filter(user=user)


# Получение всех существующих ссылок
class LinksAll(ModelViewSet):
    queryset = ShortLink.objects.all()
    serializer_class = LinksUserSerializer
