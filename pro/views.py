
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import   Loginform,RowProduitsForm, RowClientsForm
from .models import  Pumal, Clients, Produit, Wilaya
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filter import PumalFilter, ClientsFilter, NumberFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Count, Q, Sum, F
from django.views.generic import TemplateView
from django.db.models.functions import TruncMonth, ExtractMonth, Coalesce
import json





@login_required(login_url='Login')
def index(request):
    #AllProduits = Pumal.objects.all().order_by('-id')


    #context = {'AllProduits': AllProduits}
    return render(request,"indexDASH.html")


@login_required(login_url='Login')
def index2(request):
    AllProduits_list = Pumal.objects.all().order_by('-id')
    myFilter = PumalFilter(request.GET, queryset=Pumal.objects.all())
    AllProduits_list = myFilter.qs

    paginator = Paginator(AllProduits_list, 5) # Show 2 clients per page

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {'AllProduits': AllProduits_list,
               'myFilter': myFilter,
               'page_object': page_object}
    return render(request,"home3.html", context)


@login_required(login_url='Login')
def index3(request, page=1):
    AllClients_list = Clients.objects.all().order_by('-id')
    my_filter = ClientsFilter(request.GET, queryset=Clients.objects.all())
    AllClients_list = my_filter.qs




    paginator = Paginator(AllClients_list, 5) # Show 2 clients per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'AllClients': AllClients_list,
               'myFilter': my_filter,
               'page_obj': page_obj,


               }
    return render(request,"home4.html",context)


def pagelogin(request):

    uservalue = ''
    passwordvalue = ''

    log_form = Loginform()
    if request.method == "POST":
        log_form = Loginform(request.POST or None)
        if log_form.is_valid():

            uservalue = log_form.cleaned_data.get("username")
            passwordvalue = log_form.cleaned_data.get("password")

            user = authenticate(username=uservalue, password=passwordvalue)
            if user is not None:
                login(request, user)
                context = {'form': log_form,
                           'error': 'The login has been successful'}

                return redirect('Revendeurs')
                #return render(request, 'login.html', context)
            else:
                context = {'form': log_form,
                           'error': 'The username and password combination is incorrect'}

                return render(request, 'login.html', context)

    else:
        context = {'form': log_form}
        return render(request, 'login.html', context)

#def create_product(request):

        #form = ProductForm(request.POST or None)
        #if form.is_valid():
            #form.save()
        #form = ProductForm()

        #context = {
               # 'form': form
            #}
        #return render(request, "first.html", context)

@login_required(login_url='Login')
def create_product(request):
    my_form = RowProductForm()
    if request.method == "POST":
        my_form = RowProductForm(request.POST or None)
    if my_form.is_valid():
        print(my_form.cleaned_data)
        Products.objects.create(**my_form.cleaned_data )
    my_form = RowProductForm()


    context = {
        'form': my_form
    }
    return render(request, "first.html", context)


def pagelogout(request):
    if request.method == "POST":
        logout(request)

        return redirect('Login')


@login_required(login_url='Login')
def creer_produits(request):
    mon_form = RowProduitsForm()

    if request.method == "POST":
        mon_form = RowProduitsForm(request.POST or None)
    if mon_form.is_valid():
        print(mon_form.cleaned_data)
        Pumal.objects.create(**mon_form.cleaned_data )

        


    mon_form = RowProduitsForm()

    context = {
        'form': mon_form,

    }
    return render(request, "first.html", context)


@login_required(login_url='Login')
def clients(request):
    c_form = RowClientsForm()
    if request.method == "POST":
        c_form = RowClientsForm(request.POST or None)
    if c_form.is_valid():
        print(c_form.cleaned_data)
        Clients.objects.create(**c_form.cleaned_data )
    c_form = RowClientsForm()

    context = {
        'form': c_form
    }
    return render(request, "first.html", context)


def count_client(request):
    count_all = Clients.objects.all().count()
    count_ouest = Clients.objects.all().filter(région="1").count()
    count_centre = Clients.objects.all().filter(région="2").count()
    count_est = Clients.objects.all().filter(région="3").count()

    produit_nom = Produit.objects.all()
    #produit_count= Pumal.objects.all().filter(région="1",date__contains="09").aggregate(Sum('commande'))

    mynumberFilter = NumberFilter(request.GET, queryset=Pumal.objects.all())
    AllProduits_list = mynumberFilter.qs

    produit_count = AllProduits_list.values('designation__nom').annotate(
        ouest_commande=Coalesce(Sum('commande', filter=Q(région="1")), 0),
        centre_commande=Coalesce(Sum('commande', filter=Q(région="2")), 0),
        est_commande=Coalesce(Sum('commande', filter=Q(région="3")), 0)).order_by("-designation__nom")

    produit_count2 = AllProduits_list.values('designation__nom').annotate(
        ouest_commande=Coalesce(Sum('commande', filter=Q(région="1")), 0),
        centre_commande=Coalesce(Sum('commande', filter=Q(région="2")), 0),
        est_commande=Coalesce(Sum('commande', filter=Q(région="3")), 0),
        month=TruncMonth('date')).order_by("-designation__nom")


    context = {

        'count_all':count_all,
        'count_centre': count_centre,
        'count_ouest': count_ouest,
        'count_est': count_est,
        'produit_nom': produit_nom,
        'mynumberFilter': mynumberFilter,
        'AllProduits_list' : AllProduits_list,
        'produit_count': produit_count,
        'produit_count2': produit_count2,

    }

    return render(request, 'number.html', context)

def homechart (request):
    return render(request, 'count.html')

#def count_produits(request):
    #produit_count= Pumal.objects.filter(designation="13" ,région="1",date__contains="11").aggregate(Total=Sum('commande')).annotate(month=ExtractMonth('date'))

    #produit_count = Pumal.objects.values( 'région__nom','date','designation__nom').annotate(Total=Sum('commande'))

    #produit_count = Pumal.objects.values('designation','région').annotate(Total=Sum('commande')).order_by('date')

    #produit_count = Pumal.objects.filter(région= "1").annotate(month=TruncMonth('date')).values('month','designation__nom').annotate(Total=Sum('commande'))

    #produit_count = Pumal.objects.filter( designation="1" ,commande=F(id))


    #produit_count = Pumal.objects.all()
    #produit_count1= Pumal.objects.values('designation__nom').filter(région= "3").annotate(total_commande1=Sum('commande')).order_by("région")
    #produit_count2= Pumal.objects.values('designation__nom','région__nom').filter(région= "2").annotate(total_commande2=Sum('commande')).order_by("-designation__nom")
    #produit_count3= Pumal.objects.values('designation__nom','région__nom').filter(région= "3").annotate(total_commande3=Sum('commande')).order_by("-designation__nom")
    produit_count = Pumal.objects.values('designation__nom').annotate(ouest_commande=Coalesce(Sum('commande', filter= Q(région="1")),0),
                                                                    centre_commande=Coalesce(Sum('commande', filter=Q(région="2")),0),
                                                                    est_commande=Coalesce(Sum('commande', filter=Q(région="3" )),0) ).order_by("-designation__nom")




    return render(request, 'count.html', {'produit_count': produit_count,
                                          #'produit_count2': produit_count2,
                                          #"'produit_count3': produit_count3,
                                           #'produit_count':produit_count
    })

    #return JsonResponse (data={
        #'categories': categories,
        #'data': data,
        #'series' :series,
    #})



def load_wilaya(request):
    région_id = request.GET.get('région_id')
    cities = Wilaya.objects.filter(région_id=région_id).order_by('name')
    return render(request, 'dropdown_list.html', {'cities': cities})
    #print(list(wilaya.values('id','name')))
    #return JsonResponse (list(wilaya.values('id','name')),safe=False)


