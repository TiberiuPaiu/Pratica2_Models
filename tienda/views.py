from django.shortcuts import render , redirect
from tienda.models import *
from django.db.models import Q
from django.db.models import F





from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


from django.core.files.storage import FileSystemStorage
# Create your views here.

def pagina_pricipal_busar(request,id1, id2,id3):

    if id1 == 'hombre':
        if id2 == 'talla':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(Q(sexo='M') & Q(talla=id3) ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='M') & Q(talla=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto )

        if id2 == 'categoria':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(Q(sexo='M') & Q(categoria=id3) ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='M') & Q(categoria=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto )

        if id2 == 'mas_igual':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(Q(sexo='M') & Q(precio__gte=id3) ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='M') & Q(precio__gte=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto )
        if id2 == 'menos':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(Q(sexo='M') & Q(precio__lt=id3) ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='M') & Q(precio__lt=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto ) 
    if id1 == 'mujer':
        if id2 == 'talla':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'mujer', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(Q(sexo='F') & Q(talla=id3) ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'mujer', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='F') & Q(talla=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto )
        if id2 == 'categoria':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'mujer', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(Q(sexo='F') & Q(categoria=id3) ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'mujer', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='F') & Q(categoria=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto )
        if id2 == 'mas_igual':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'mujer', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(Q(sexo='F') & Q(precio__gte=id3) ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'mujer', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='F') & Q(precio__gte=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto )
        if id2 == 'menos':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'mujer', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(Q(sexo='F') & Q(precio__lt=id3) ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'mujer', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='F') & Q(precio__lt=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto ) 
    if id1 == 'sin':
        if id2 == 'talla':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( talla=id3 ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(  Q(talla=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto )
        if id2 == 'categoria':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(categoria=id3 ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(categoria=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto )
        if id2 == 'mas_igual':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(precio__gte=id3 ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(precio__gte=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto )
        if id2 == 'menos':
            if request.user.is_authenticated:
                contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( precio__lt=id3 ) }
                return render(request, "pagina_principal.html", contexto )
            else:
                contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(precio__lt=id3) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto ) 
    
def pagina_pricipal_busar_input(request, id1):
    palabra=request.GET['buscar']
    if id1 == 'sin':
        if request.user.is_authenticated:
                contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( nombre__icontains=palabra ) }
                return render(request, "pagina_principal.html", contexto )
        else:
                contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(nombre__icontains=palabra) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto ) 
    if id1 == 'mujer':
        if request.user.is_authenticated:
                contexto = { 'sexo': 'mujer', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='F') & Q(nombre__icontains=palabra) ) }
                return render(request, "pagina_principal.html", contexto )
        else:
                contexto = { 'sexo': 'mujer', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='F') & Q(nombre__icontains=palabra) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto ) 
    if id1 == 'hombre':
        if request.user.is_authenticated:
                contexto = { 'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='M') & Q(nombre__icontains=palabra) ) }
                return render(request, "pagina_principal.html", contexto )
        else:
                contexto = { 'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='M') & Q(nombre__icontains=palabra) & Q(desquento_procentaje=0 ) ) }
                return render(request, "pagina_principal.html", contexto )     

def pagina_pricipal(request):
    
    if request.user.is_authenticated:
        contexto = {  'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.all()}
        return render(request, "pagina_principal.html", contexto )
    else:
        contexto = { 'sexo': 'sin', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( desquento_procentaje=0  )}
        return render(request, "pagina_principal.html", contexto )

def pagina_pricipal_h(request):  
    if request.user.is_authenticated:
        contexto = {  'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(sexo='M')}
        return render(request, "pagina_principal.html", contexto )
    else:
        contexto = {  'sexo': 'hombre', 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='M') & Q(desquento_procentaje=0 ) )}
        return render(request, "pagina_principal.html", contexto )
def pagina_pricipal_f(request):
    if request.user.is_authenticated:
        contexto = {  'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter(sexo='F')}
        return render(request, "pagina_principal.html", contexto )
    else:
        contexto = { 'categorias': Categoria.objects.all() ,'productos': Producto.objects.filter( Q(sexo='F') & Q(desquento_procentaje=0 ) )}
        return render(request, "pagina_principal.html", contexto )


# para añadir un producto
def add_product(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='trabajador').exists():
            contexto = { 'colores':  Color.objects.all(), 'categorias': Categoria.objects.all() }
            return render(request, "pagina_stock.html", contexto  )
        else:
            return redirect('/accounts/login/')
    else:
        return redirect('/accounts/login/')
            

def add_post_product(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='trabajador').exists():
            if request.method == "POST":
                #if request.FILES.get('foto')
                img = request.FILES["foto"]
                request.POST['categoria']
                tipo = Categoria.objects.get(pk = request.POST['categoria'])
                c= Color.objects.get(pk = request.POST['color'])
                producto = Producto.objects.create(nombre= request.POST['nombre'],unidades= request.POST['unidades'],precio= request.POST['precio'],desquento_procentaje=request.POST['desquento_procentaje'],categoria=tipo ,talla= request.POST['talla'],sexo= request.POST['Sexo'],color= c,ruta_img=img.name )
                fs = FileSystemStorage()
                
                fs.save(img.name,img)
                producto.save()
                
                contexto = {'error': "text-success", 'mensaje': img.name, 'colores':  Color.objects.all(), 'categorias': Categoria.objects.all() }
                return render(request, 'pagina_stock.html', contexto)
            else:
                contexto = {'error': "text-danger",'mensaje': "Se ha porducido un error", 'colores':  Color.objects.all(), 'categorias': Categoria.objects.all() }
                return render(request, 'pagina_stock.html', contexto)
        else:
            return redirect('/accounts/login/')
    else:
        return redirect('/accounts/login/')
    
# para hacer el direconameto de los dos roles
def validar_usuario(request):

    if request.user.is_authenticated:
        if request.user.groups.filter(name='trabajador').exists():
            return redirect('/producto_add/')
        if request.user.groups.filter(name='cliente').exists():
            return redirect('/')
        else:
            return redirect('/accounts/login/')
    else:
        return redirect('/accounts/login/')



def registrar_cliente(request):
    
    return render(request, "pagina_registrarse.html",{})

def from_cliente(request):
    contexto={}
    if request.method == "POST":
        if  len(request.POST['password']) >= 8 and request.POST['email'] != None and request.POST['username'] != None and User.objects.filter(username=request.POST['username']).exists() == False :

            user = User.objects.create_user(request.POST['username'],request.POST['email'], request.POST['password'])
            group = Group.objects.get(name='cliente')
            user.groups.add(group)
            user.last_name =request.POST['lastname']
            user.first_name=request.POST['firstname']
            user.save()
            cliente = Cliente.objects.create(user = user,tarjeta = request.POST['trjeta'],preferencia = request.POST['exampleRadios'])
            cliente.save()
        
            return redirect('/accounts/login/')
        else:
            contexto={'mensaje': "Se ha porducido un error"}
            return render(request, 'pagina_registrarse.html', contexto)
    else:
        return redirect('/registrate/')


def add_compra(request,id):

    if request.user.is_authenticated:
        precio= Producto.objects.get(pk=id).precio
        desquento=Producto.objects.get(pk=id).desquento_procentaje
        aplicar_descuento= float((desquento * precio) / 100)
        precio_actual= float( precio - aplicar_descuento)
        id_user_actual=User.objects.get(username=request.user.username)
        compra = Compra.objects.create( author = id_user_actual , id_produc=Producto.objects.get(pk=id), precio_desquento=precio_actual )
        compra.save()
        return redirect('/')
    else:
        return redirect('/accounts/login/')    

def view_compra(request):
    if request.user.is_authenticated:
        pk=User.objects.get(username=request.user.username).pk
        compra=Compra.objects.filter( author= pk )
        total = 0.0
        for c in compra:
            total = total + c.precio_desquento


        contexto = { 'categorias': Categoria.objects.all() ,'compra': compra,'total':str(total)}
        return render(request, 'pagina_compra.html', contexto)
    else:
        return redirect('/accounts/login/') 