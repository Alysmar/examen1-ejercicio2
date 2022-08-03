from xmlrpc.server import SimpleXMLRPCServer  
import sys
import datetime
#importamos el modulo de xmlrpc para hacer el servidor 




#
inventario = {
    "pantalon": 300,
    "camisa": 100,
    "zapatos":20 
}


# generamos una funcion que es la que usara el cliente. 
# funcion para consultar un objeto en el inventario
def consultar_producto(obj):
    if obj in inventario:
        return inventario[obj]

#funcion para ver la lista completa del inventario
def inventario_completo():
    return inventario
        
        

# definimos un puerto por donde estara habilitada la conexion de los clientes
server = SimpleXMLRPCServer(("localhost", 6789),allow_none=True)

# registramos la funciones que estaran disponibles a nuestro cliente.
server.register_function(consultar_producto, "consultar_producto")
server.register_function(inventario_completo, "inventario_completo")




#mensaje de bienvenida para nuestros usuarios
print("Se ha iniciado  el servidor RPC", datetime.datetime.now())
print("Para detenerlo pulse 'crtl + C'")

try:
#intentamos conectarnos en caso tal de que exista un error   
    server.serve_forever()

except KeyboardInterrupt:
#interrumpimos la conexion con crtl+ c  
    print("\nSe ha desactivado el servidor RPC", datetime.datetime.now())
    sys.exit(0)




