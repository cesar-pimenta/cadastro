from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

# Register your models here.

class PalestranteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tema', 'palestrante', 'cargo', 'resumo', 'email', 'telefone', )
    search_fields = ('palestrante')

class PalestranteImport(ImportExportModelAdmin):
    pass

admin.site.register(Palestrante,PalestranteImport),