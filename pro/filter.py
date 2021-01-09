import django_filters
from .models import Pumal, Clients


class PumalFilter(django_filters.FilterSet):
    class Meta:
        model = Pumal
        fields = ['client', 'designation', 'région','wilaya']



class ClientsFilter(django_filters.FilterSet):
    class Meta :
        model = Clients
        fields = ['nom']

class NumberFilter(django_filters.FilterSet):

    class Meta:
        model = Pumal
        #fields = ['date']
        fields = {
           'date': ['month'],


       }


