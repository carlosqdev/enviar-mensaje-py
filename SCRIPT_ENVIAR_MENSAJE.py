#URl:
# xxxx&nombre=Layla&apellido=Scheli&edad=31&estatura=1.65
# xxxx&nombre=Layla&apellido=Scheli
# xxxx&nombre=Layla

#Importamos la librería para generar mensajes de log en la ejecución de la función
import logging

#Importamos la librería de azure functions para implementar funciones
import azure.functions as func

#Definimos la función "main" que recibe la petición de procesamiento
#La petición de procesamiento es colocada en la variable "req"
def main(req : func.HttpRequest) -> func.HttpResponse:
    #Respuesta que devolverá la función
    #Inicialmente está vacía
    respuesta = None

    #Verificamos si la función recibió todos los
    #parámetros que necesita para funcionar
    if(
        (req.params.get("nombre") != None) &
        (req.params.get("apellido") != None) &
        (req.params.get("edad") != None) &
        (req.params.get("estatura") != None)
    ):
        #Extraemos cada parámetro
        nombre = req.params.get("nombre")
        apellido = req.params.get("apellido")
        edad = int(req.params.get("edad"))
        estatura = float(req.params.get("estatura"))

        #Mostramos en el log los parámetros
        logging.info("Nombre recibido: "+nombre)
        logging.info("Apellido recibido: "+apellido)
        logging.info("Edad recibida: "+str(edad))
        logging.info("Estatura recibida: "+str(estatura))

        #Construimos la respuesta
        respuesta = func.HttpResponse(f"Hola {nombre} {apellido}, tu edad es {edad} y tu estatura es {estatura}")
    else:
        #Indicamos en la respuesta que hay un error
        respuesta = func.HttpResponse(f"Debe agregar todos los parametros (nombre, apellido, edad y estatura)")
    
    #Retornamos la respuesta    
    return respuesta
