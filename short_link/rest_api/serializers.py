from rest_framework.serializers import ModelSerializer
from links.models import ShortLink


# Сериалайзер ссылок отдельного пользователя.
class LinksUserSerializer(ModelSerializer):
    class Meta:
        model = ShortLink
        fields = ['original_link', 'shortened_link']


# Сериалайзер ссылок всех пользователя.
class LinksAllSerializer(ModelSerializer):
    class Meta:
        model = ShortLink
        fields = '__all__'
