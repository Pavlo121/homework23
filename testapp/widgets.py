from django.forms.widgets import Select

class Widget(Select):
    def __init__(self, attrs=None, choices=()):
        default_attrs = {'class': 'custom-select'}  # Добавляем CSS-класс
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs, choices=choices)  # Вызываем родительский конструктор
