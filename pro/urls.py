from django.urls import path
from . import views


urlpatterns = [
    path('', views.index2, name='Home'),
    path('create', views.create_product, name= 'Create'),
    path('login', views.pagelogin, name='Login'),
    path('logout', views.pagelogout, name='Logout'),
    path('revendeurs', views.creer_produits, name='Revendeurs'),
    path('Disponibilté', views.index2, name='Disponibilté'),
    path('Nouveau_Client', views.clients, name='Nouveau_Client'),
    path('Liste_Des_Clients', views.index3, name='Liste_Des_Clients'),
    #path('dashboard', views.index, name= 'dashboard'),
    path('number', views.count_client, name='number'),
    #path('number', views.count_produits, name= 'number'),
    #path('count', views.count_produits, name= 'count'),
    path('load-wilaya', views.load_wilaya, name='load-wilaya'),





]