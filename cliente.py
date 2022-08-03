import xmlrpc.client
import threading
import time

# mensaje de bienvenida
print ("Bienvenido a la base de datos")
print ("escriba 'EXIT' o 'exit' para salir")


#hacemos una varaible llamada proxy la cual tendra la comunicacion con nuestro servidor
proxy = xmlrpc.client.ServerProxy("http://localhost:6789")

#funcion que llama a una de las funciones de nuestro servidor
# funcion para ver un objeto en el inventario
def conectar_sevidor(obj):
    result= proxy.consultar_producto(obj)
    return result

# funcion para ver el inventario
def conectar_sevidor_2():
    inventario= proxy.inventario_completo()
    for i in inventario:
        print(i, ":" , inventario[i])

# funcion para obtener las entradas del usuario
def get_input():
    data = input() 
    return data    

# funcion con mensaje de despedida
def despedida():
     print("\ndesconectando...")
     time.sleep(2)
     print("Gracias por consultar en la base de datos")

while True:
    try:
        
        # se coloca tiempo de 2 segundos para una respuesta un poco menos agresiva.
        # opciones al usuario
        
        time.sleep(2)
        print ("\nSeleccione una de las siguientes opciones:")
        print ("\n1. Ver todo el Inventario")
        print ("2. Buscar prenda")
        print ("3. Salir")
        opcion=get_input()
        
        if opcion == "1":
            print ("\nBuscando.....")
            print(" ")
            # peticion al servidor del inventario  
            conectar_sevidor_2()
            
        elif opcion == "3":
            despedida()
            break
        else:
            # si selecciona 2 entramos en un bucle para buscar la prenda por nombre.
            while True:
                print ("\nIngresa el nombre de una prenda de ropa:")
                obj=get_input()
                if obj == "exit" or  obj == "EXIT":
                    despedida()
                    break
                print ("\nBuscando.....")
                # peticion al servidor para buscar una prenda
                result=conectar_sevidor(obj)
                
                
                # si no existe la prenda mandara este msj
                
                if result is None:
                    print("\nLo siento no se pudo encontrar la prenda de ropa")
                    print("Intente escribir algo diferente")
                    
                else:
                # si  existe la prenda mandara este msj
                    
                    print(f"El precio de {obj} es de: {result}")
                
                
                # msj al usuario si quiere continuar buscando prendas individualmente
                time.sleep(2)
                print ("\n¿Desea buscar otra prenda de ropa?")
                print ("escriba cualquier tecla o  'NO' para salir:")
                
                # en caso de salir volvemos a las primeras opciones
                
                salir=get_input()
                if salir == "NO" or  salir == "no":
                    break    
    except:
        print("\nno se pudo conectar al servidor")     





