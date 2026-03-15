# declaracion de variables
carrito = []
catalogo = [
    {"id":1,"nombre":"ampolleta","categoria":"hogar","precio":2500},
    {"id":2,"nombre":"Smart TV","categoria":"tecnologia","precio":259990}
]

# definición de funciones
def mostrar_menu():
    print("Bienvenido a la tienda")
    print("(1) Ver catálogo")
    print("(2) Buscar producto")
    print("(3) Agregar producto al carrito")
    print("(4) Ver carrito y total")
    print("(5) Vaciar carrito")
    print("(0) Salir")

    

def listar_productos():
    if(len(catalogo)<=0):
        print("No hay productos en el catálogo. Volviendo al menú")
    else:
        for p in catalogo:
            print(f"ID: {p["id"]} \n Producto: {p["nombre"]} \n Categoría: {p["categoria"]} \n Precio: ${p["precio"]}")

# ejecución principal
while True:
    mostrar_menu()
    opcion = int(input("Ingrese la opción deseada: "))
    if (opcion==1):
        #catalogo
        listar_productos()

    elif (opcion==2):
        #buscar
        print("")
    elif (opcion==3):
        #agregar al carro
        print("")
    elif (opcion==4):
        #mostrar carrito
        print("")
    elif (opcion==5):
        #vaciar carrito
        print("")
    elif (opcion==0):
        #salir
        print("Saliendodoooodo")
        break
    else:
        #mostrar error
        print("opcion no válida...")