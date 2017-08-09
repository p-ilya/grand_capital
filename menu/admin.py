from django.contrib import admin
from .models import MenuNode


# Register your models here.


class MenuNodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    exclude = ('level',)


admin.site.register(MenuNode, MenuNodeAdmin)
