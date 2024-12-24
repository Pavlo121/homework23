from django.contrib import admin
from .models import UpperCaseText

class UpperCaseTextAdmin(admin.ModelAdmin):
    list_display = ['text', 'word_count']
    list_filter = ['text']
    actions = ['uppercase_action']

    def uppercase_action(self, request, queryset):
        for obj in queryset:
            obj.text = obj.text.upper()
            obj.save()

admin.site.register(UpperCaseText, UpperCaseTextAdmin)

#user
#password 1234