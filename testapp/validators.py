from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if len(value) != 10 or not value.isdigit():
        raise ValidationError('Номер телефону має складатися з 10 цифр.')
