from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico

# Create your views here.
# renderizar es pintar
def Home(request):
    return render(request,'index.html')

def Medicos (request):
    #debo utilizar la clase formularioMedico
    #Creamos asi un objeto
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario
    }
    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=='POST':
        #VALIDAR SI LOS DATOS SON CORRECTOS
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            print(datos)

    return render(request,'registrosmedicos.html',diccionario)



    