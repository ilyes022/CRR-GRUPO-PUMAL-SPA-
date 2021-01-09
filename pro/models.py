from django.db import models
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)







class Pumal (models.Model):
    date = models.DateField()
    client = models.ForeignKey('Clients', on_delete=models.CASCADE, default='true')
    région = models.ForeignKey('Location', on_delete=models.CASCADE, default='true')
    wilaya = models.ForeignKey('Wilaya', on_delete=models.SET_NULL, null=True)
    designation = models.ForeignKey('Produit',on_delete=models.CASCADE, default="true")
    disponibilité = models.CharField(max_length=255)
    quantité_disponible = models.IntegerField()
    commande = models.IntegerField()
    description =models.CharField(max_length=255)
    disponibilité_concurrent = models.CharField(max_length=255)
    created_by = models.CharField(max_length=100)
    créer_par = CurrentUserField()





    class Meta:
        ordering = ["-date"]





class Clients (models.Model):
    région = models.ForeignKey('Location', on_delete=models.CASCADE, default='true')
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    wilaya = models.ForeignKey('Wilaya', on_delete=models.SET_NULL, null=True)
    localité = models.CharField(max_length=255)
    nom_gérant = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    téléphone = models.CharField(max_length=255)
    potentiel = models.CharField(max_length=255)
    distributeur = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
    class Meta:
        ordering = ["-id"]

class Location (models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom



class Produit (models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    ordering = ["-id"]

class Wilaya (models.Model) :
    région = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name