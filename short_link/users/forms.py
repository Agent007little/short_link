from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    # Определяю метод валидации для пароля, в наследуемом классе только проверка второго пароля.
    # def clean_password1(self):
    #     password1 = self.cleaned_data['password1']
    #     if len(password1) < 8:
    #         raise ValidationError("Пароль должен быть не меньше 8 символов")
    #     elif re.search('[0-9]', password1) is None:
    #         raise ValidationError("Убедитесь, что в вашем пароле есть цифра")
    #     elif re.search('[A-ZА-Я]', password1) is None:
    #         raise ValidationError("Убедитесь, что ваш пароль содержит заглавную букву")
    #
    #     return password1

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserOurRegistration, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
