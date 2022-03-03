from django.contrib import admin

from products.models import ProductCategory, Product

admin.site.register(Product)


#@admin.register(Product)
#class ProductsAdmin(admin.ModelAdmin):
#    list_display = ('name', 'price', 'quantity', 'category'),
#    fields = ('name', 'price', 'quantity', 'category'),
#    search_fields =  ('name',),
 #   ordering = ('name',),


admin.site.register(ProductCategory)