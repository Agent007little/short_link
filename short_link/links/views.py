from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import LinkForm
from .models import ShortLink


# Вывод главной страницы
def home_page(request):
    return render(request, 'links/home_page.html', {'title': 'Сократи.ру'})


# Страница описания
def about_us(request):
    return render(request, 'links/about_us.html', {'title': 'Сократи.ру'})


# Класс отвечает за страницу на которой сокращают ссылки
class Shorten(DetailView):
    model = ShortLink
    template_name = 'links/shorten_link.html'

    # функция для получения модели ShortLink текущего пользователя
    def get_object(self, queryset=None):
        user = self.request.user
        return ShortLink.objects.filter(user=user)

    # get запрос, отображение формы и списка ссылок
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Shorten, self).get_context_data(**kwargs)
        user_links = self.get_object()
        context['user_links'] = user_links

        link_form = LinkForm()
        context['link_form'] = link_form
        return context

    # Post запрос
    def post(self, request, *args, **kwargs):
        link_form = LinkForm(request.POST)
        user_links = self.get_object()
        variables = {
            'link_form': link_form,
            'user_links': user_links
        }
        # сохранение формы если данные верные
        if link_form.is_valid():
            obj = link_form.save(commit=False)
            obj.user = request.user
            obj.save()
            link_form.save_m2m()
            return redirect('/shorten/')
        else:
            # Дописываю костыли, почему-то текст при проверке на длину original_link не меняется в форме
            try:  # Проверка на ошибку. Если это поле введено верно - ошибка игнорируется
                if link_form.errors['original_link']:
                    link_form.errors['original_link'][0] = 'Ссылка должна быть не длиннее 250 символов.'
            except Exception as e:
                print(e)
            return render(request, 'links/shorten_link.html', variables)
