from django.contrib import admin
from .models import Fruit 
# Register your models here.
class FruitAdmin(admin.ModelAdmin):
  readonly_fields = ("slug",)

admin.site.register(Fruit,FruitAdmin)
