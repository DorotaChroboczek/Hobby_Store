from django.contrib import admin

from .models import Overcategory, Category, Subcategory, MetaProduct, \
    UnitOfMeasurement, Product, ProductPromotion, Order, OrderItem


@admin.register(Overcategory)
class OvercategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'overcategory', 'image')


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'image')


@admin.register(MetaProduct)
class MetaProductAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'name', 'description', 'image')


@admin.register(UnitOfMeasurement)
class UnitOfMeasurementAdmin(admin.ModelAdmin):
    list_display = ('symbol',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('meta_product', 'measure', 'package',
                    'price', 'availability')


@admin.register(ProductPromotion)
class ProductPromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'package', 'measure', 'price',
                    'standard_price', 'percentage_of_the_promotion')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_ordered', 'complete')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')

