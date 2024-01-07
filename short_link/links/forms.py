from django import forms
from django.core.exceptions import ValidationError

from .models import ShortLink


# Форма добавления ссылки пользователя
class LinkForm(forms.ModelForm):

    original_link = forms.URLField(label='Полная ссылка', max_length=250, required=True)
    shortened_link = forms.CharField(label='Сокращённая ссылка')

    # Проверка на длину оригинальной ссылки.
    def clean_original_link(self):
        original_link = self.cleaned_data['original_link']
        if len(original_link) > 250:
            raise ValidationError('Ссылка должна быть не длиннее 250 символов.')
        return original_link

    # Проверка на уникальность сокращения ссылки
    def clean_shortened_link(self):
        shortened_link = self.cleaned_data['shortened_link']
        if ShortLink.objects.filter(shortened_link=shortened_link).exists():
            raise ValidationError('Такое сокращение уже существует')
        return shortened_link

    class Meta:
        model = ShortLink
        fields = ['original_link', 'shortened_link']
