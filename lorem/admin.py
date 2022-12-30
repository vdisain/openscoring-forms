from django.contrib import admin
from .models import Lorem

class LoremAdmin(admin.ModelAdmin):
    model = Lorem
    list_display = ('created', 'text_field')
    exclude = ('session_key',)

admin.site.register(Lorem, LoremAdmin)