from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from .forms import RegisterForm,ConnexionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse

def index(request):
    """Page d'accueil du site"""
    text = """<h1>Bienvenue sur le meilleur site de troc de france!</h1>
              <p>Troquez tout ce que vous voulez et gagner de l'argent sans rien faire !</p>"""
    return HttpResponse(text)

def view_troc(request,id_cat,id_troc):
    """ Vue qui affiche le troc demandé """
    if int(id_troc)>100:
        raise Http404
    return HttpResponse("<h1>Voici le troc numéro {} de la categorie {}!</h1> <p>test affichage argument GET: {}</p>".format(id_troc,id_cat,request.GET['ref']))

def index2(request):
    """Page d'accueil du site"""
    message1 = "Bonjour Thom"
    message2= "bien ou bien"
    message3= "tranquille la mif"
    message4="Appuie la je te nique ta race"
    return render(request,'index.html',{'message1':message1,'message2':message2,'message3':message3,'message4':message4})


def register(request):
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        new_login = form.cleaned_data['username']
        new_passwd = form.cleaned_data['password']
        new_adr_mail= form.cleaned_data['adresse_mail']
        
        user = User.objects.create_user(new_login,new_adr_mail, new_passwd)
        user.save()
        return render(request,"bravo.html",{'login':new_login})
    return render(request,"register.html",locals())

def connexion(request):
    error = False
    
    if request.method=="POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
            else:
                error=True
    else:
        form = ConnexionForm()
    return render(request,'connect.html',locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))  
