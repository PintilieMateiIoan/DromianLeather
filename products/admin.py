from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'price', 'pub_date', 'related',
                           'img_path', 'img_description']})
    ]
    list_display = ('name', 'price', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['name', 'price']

admin.site.register(Product, ProductAdmin)
