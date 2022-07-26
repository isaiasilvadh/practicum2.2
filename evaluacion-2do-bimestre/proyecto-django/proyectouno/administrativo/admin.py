from django.contrib import admin

# Register your models here.

from administrativo.models import Cliente, MarcaMedidor, Medidor

class ClienteAdmin(admin.ModelAdmin):

    list_display = ('identificacion', 'correo')
    search_fields = ('identificacion', 'correo')

admin.site.register(Cliente, ClienteAdmin)

class MarcaMedidorAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'origen')
    search_fields = ('nombre', 'origen')

admin.site.register(MarcaMedidor, MarcaMedidorAdmin)


class MedidorAdmin(admin.ModelAdmin):
    list_display = ('marca', 'costoMedidor', 'origen', 'cliente', 'direccion', 'parroquia')
    raw_id_fields = ('marca', 'cliente',)

admin.site.register(Medidor, MedidorAdmin)
