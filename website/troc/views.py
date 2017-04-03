from django.http import HttpResponse,Http404
from django.shortcuts import render
from .forms import RegisterForm
from .models import Client


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
        new_login = form.cleaned_data['login']
        new_passwd = form.cleaned_data['passwd']
        
        new_client = Client(login=new_login,passwd=new_passwd)
        new_client.save()
        return render(request,"bravo.html",{'login':new_login})
    return render(request,"register.html",locals())

def connect(request):
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        new_login = form.cleaned_data['login']
        new_passwd = form.cleaned_data['passwd']
        
        try:
            Client.objects.get(login=new_login,passwd=new_passwd)
            return render(request,"bravo.html",{'login':new_login})
        except:
            message="Login ou mot de passe incorrect, veuillez réessayer"
            return render(request, 'connect.html', locals())
    return render(request, 'connect.html', locals())

    
