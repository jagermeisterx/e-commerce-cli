# declaracion de variables
carrito = []
catalogo = [
    {"id": 1,  "nombre": "Ampolleta LED",          "categoria": "hogar",       "precio": 2500},
    {"id": 2,  "nombre": "Smart TV 55\"",           "categoria": "tecnologia",  "precio": 259990},
    {"id": 3,  "nombre": "Polera básica",           "categoria": "ropa",        "precio": 9990},
    {"id": 4,  "nombre": "Jeans slim fit",          "categoria": "ropa",        "precio": 24990},
    {"id": 5,  "nombre": "Audífonos bluetooth",     "categoria": "tecnologia",  "precio": 49990},
    {"id": 6,  "nombre": "Teclado mecánico",        "categoria": "tecnologia",  "precio": 39990},
    {"id": 7,  "nombre": "Lámpara de escritorio",   "categoria": "hogar",       "precio": 14990},
    {"id": 8,  "nombre": "Cojín decorativo",        "categoria": "hogar",       "precio": 7990},
    {"id": 9,  "nombre": "Zapatillas running",      "categoria": "ropa",        "precio": 34990},
    {"id": 10, "nombre": "Mouse inalámbrico",       "categoria": "tecnologia",  "precio": 19990},
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
        hacer_separador(30)
        for p in catalogo:
            print(f"ID: {p["id"]} \n Producto: {p["nombre"]} \n Categoría: {p["categoria"]} \n Precio: ${p["precio"]}")
            hacer_separador(30)

def buscar_producto(catalogo):
    busqueda = input("Ingresa nombre o categoría a buscar: ").strip().lower()   #.strip() borra espacios innecesarios y .lower() los deja en minusculas
    resultados = []
    for p in catalogo:
        nombre_coincide    = busqueda in p["nombre"].lower()
        categoria_coincide = busqueda in p["categoria"].lower()

        if (nombre_coincide or categoria_coincide):
            resultados.append(p)

    if len(resultados) == 0:
        print("Producto no encontrado ...")
    else:
        hacer_separador(50)
        print(f"Se encontraron {len(resultados)} resultado(s):")
        for producto in resultados:
            print(f" ID: [{producto['id']}] {producto['nombre']}")
            print(f"      Categoría : {producto['categoria']}")
            print(f"      Precio    : ${producto['precio']}")
            hacer_separador(50)
            
def hacer_separador(cantidad):
    print("*" * cantidad)




# ejecución principal
while True:
    mostrar_menu()
    opcion = int(input("Ingrese la opción deseada: "))
    if (opcion==1):
        #catalogo
        listar_productos()

    elif (opcion==2):
        buscar_producto(catalogo)
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