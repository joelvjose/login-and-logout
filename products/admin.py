from django.contrib import admin
from .models import product,discount

class producAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','image')

class discountAdmin(admin.ModelAdmin):
    list_display = ('code','description','discount')
    
# Register your models here.
admin.site.register(product,producAdmin)
admin.site.register(discount,discountAdmin)