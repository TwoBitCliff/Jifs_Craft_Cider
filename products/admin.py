from django.contrib import admin
from .models import Product, Category, Reviews

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_id',
        'name',
        'category',
        'price',
        'quantity',
        'image',
        'rating',       
    )

    ordering = ('product_id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'product_id', 'body', 'created_on', 'active')
    list_filter = ('created_on', 'active')
    search_fields = ('user_profile', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
