from django import forms
from .models import  Pumal, Clients, Location, Produit, Wilaya
from django import forms
from django.forms import ModelChoiceField
from django.db.models import F
from datetimepicker.widgets import DateTimePicker
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.utils import timezone
from django.utils import formats, translation
from django.contrib.admin import widgets












class Loginform(forms.Form):
    username= forms.CharField(max_length= 25,label="Username")
    password= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)


class ProduitsForm(forms.ModelForm):
    class Meta:
        model = Pumal
        fields = [
            #'date',
            'client',
            'région',
            'wilaya',
            'designation',
            'disponibilité',
            'quantité_disponible',
            'commande',
            'description',
            'disponibilité_concurrent'
        ]



puma = [
    ('..', '..'),
    ('PUMA CE BLANC	PUMA', 'PUMA CE BLANC	PUMA'),
    ('PUMA CE GRIS', 'PUMA CE GRIS'),
    ('MORCEM COLOR J U BLANCO 154', 'MORCEM COLOR J U BLANCO 154'),
    ('MORCEM COLOR J U BEIGE 172', 'MORCEM COLOR J U BEIGE 172'),
    ('MORCEM COLOR J U CHOCOLAT 164', 'MORCEM COLOR J U CHOCOLAT 164'),
    ('MORCEM COLOR J U GRIS MACAEL 157', 'MORCEM COLOR J U GRIS MACAEL 157'),
    ('MORCEM COLOR J U GRIS  156', 'MORCEM COLOR J U GRIS  156'),
    ('MORCEM COLOR J U CHOCOLAT 164', 'MORCEM COLOR J U CHOCOLAT 164'),
    ('MORCEM COLOR J U NEGRO E243 05 KG	', 'MORCEM COLOR J U CHOCOLAT 164'),
]
choix2 = [
    ('..', '..'),
    ('oui', 'Oui'),
    ('non', 'Non'),
]



class RowProduitsForm(forms.Form):
    date = forms.DateField(help_text="Please use the following format: <em>Mois/Jour/Année</em>.")
    client = forms.ModelChoiceField(queryset=Clients.objects.all())
    région = forms.ModelChoiceField(queryset=Location.objects.all())
    wilaya = forms.ModelChoiceField(queryset=Wilaya.objects.all())
    designation = forms.ModelChoiceField(queryset=Produit.objects.all())
    disponibilité = forms.CharField(widget=forms.Select(choices= choix2))
    quantité_disponible = forms.IntegerField()
    commande = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea, required= False)
    disponibilité_concurrent = forms.CharField(widget=forms.Select(choices= choix2))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wilaya'].queryset = Wilaya.objects.none()

        if 'région' in self.data:
            try:
                région_id = int(self.data.get('région'))
                self.fields['wilaya'].queryset = Wilaya.objects.filter(région_id=région_id).order_by('name')

            except (ValueError, TypeError):
               pass   #invalid input from the client; ignore and fallback to empty City queryset
        #elif self.instance.pk:
            #self.fields['wilaya'].queryset = self.instance.région.wilaya_set.order_by('name')




class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = [
            'région',
            'nom',
            'type',
            'wilaya',
            'localité',
            'nom_gérant',
            'adresse',
            'téléphone',
            'potentiel',
            'distributeur',
        ]
type_client = [
    ('..','..'),
    ('ceramiste', 'Ceramiste'),
    ('materiaux de construction', 'Materiaux De Construction'),
    ('quincaillerie', 'Quincaillerie'),

]
#wiliya_client = [
    #('..','..'),
    #('alger', 'Alger'),
    #('oran', 'Oran'),

#]
localité_client = [

    ('..','..'),
    ('belarbi', 'Belarbi'),
    ('ben badis', 'Ben Badis'),

]
potentiel_client = [
    ('..','..'),
    ('fort','Fort'),
    ('moyen','Moyen'),
    ('faible','Faible'),
]

distributeur_client = [
    ('..','..'),
    ('bs mat','Bs Mat'),
    ('bouali','Bouali'),

]
type_location = [
    ('centre','Centre'),
    ('est','Est'),
]

class RowClientsForm(forms.Form):
    région = forms.ModelChoiceField(queryset=Location.objects.all())
    nom = forms.CharField()
    type = forms.CharField(widget=forms.Select(choices= type_client))
    wilaya = forms.ModelChoiceField(queryset=Wilaya.objects.all())
    localité = forms.CharField(widget=forms.Select(choices= localité_client))
    nom_gérant = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    téléphone = forms.IntegerField()
    potentiel = forms.CharField(widget=forms.Select(choices= potentiel_client))
    distributeur = forms.CharField(widget=forms.Select(choices= distributeur_client))


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'nom',
        ]

