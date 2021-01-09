from django.contrib import admin
from .models import  Pumal, Clients, Location, Produit, Wilaya


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


#admin.site.register(Products, ProductAdmin)

class PumalAdmin(admin.ModelAdmin):
    list_display = ('client','région','wilaya','designation','disponibilité','quantité_disponible','commande','description','disponibilité_concurrent','date','créer_par')

admin.site.register(Pumal,PumalAdmin)




class ClientsAdmin(admin.ModelAdmin):
    list_display = ('nom','type','wilaya','distributeur')

admin.site.register(Clients, ClientsAdmin)




admin.site.register(Location)


admin.site.register(Produit)

admin.site.register(Wilaya)


