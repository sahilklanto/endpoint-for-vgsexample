from django.contrib import admin
from api.models import SaveData


class SaveDataModelAdmin(admin.ModelAdmin):
    readonly_fields = ['date_created']

admin.site.register(SaveData, SaveDataModelAdmin)

# Register your models here.
