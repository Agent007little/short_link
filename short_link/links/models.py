from django.db import models
from django.contrib.auth.models import User


class ShortLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_link = models.URLField(max_length=250,
                                    error_messages={'max_length': 'Ссылка должна быть не длиннее 250 символов.'})
    shortened_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Проверка на уникальность сокращений ссылок у каждого пользователя отдельно
        unique_together = ('user', 'shortened_link')

    def __str__(self):
        return self.shortened_link
