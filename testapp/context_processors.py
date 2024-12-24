from datetime import datetime
from ipware import get_client_ip


def site_settings(request):
    """Додає загальні налаштування сайту у всі шаблони."""
    return {
        'site_name': 'Мій дивовижний сайт',
        'current_year': 2024,
    }

def current_date(request):
    """Добавляет текущую дату контекст шаблона."""
    return {'date': datetime.now()}


def user_ip(request):
    """
    Получает IP-адрес клиента из запроса.
    Возвращает '0.0.0.0', если IP определить не удалось.
    """
    ip, is_routable = get_client_ip(request)
    return {'user_ip': ip, 'is_routable': is_routable}


def my_site_settings(request):
    """Добавляет общие настройки сайта во все шаблоны."""
    return {
        'site_name': 'Мій сайт',
        'current_year': datetime.now().year,
    }