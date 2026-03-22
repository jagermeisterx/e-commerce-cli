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
    hacer_separador(35)
    print("*    Bienvenido a la tienda       *")
    print("-----------------------------------")
    print("* (1) Ver catálogo                *")
    print("* (2) Buscar producto             *")
    print("* (3) Agregar producto al carrito *")
    print("* (4) Ver carrito y total         *")
    print("* (5) Vaciar carrito              *")
    print("* (0) Salir                       *")   
    hacer_separador(35) 

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


def agregar_al_carrito(catalogo, carrito):
    hacer_separador(35)
    try:
        id_input = int(input("Ingresa el ID del producto: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        return

    # buscar el producto en el catálogo con .next() la primera es la condición y si no encuentra queda como none
    producto = next(
        (p for p in catalogo if p["id"] == id_input),
        None
    )

    if producto is None:
        print(f"No existe ningún producto con ID {id_input}.")
        return

    # pedir y validar la cantidad
    try:
        cantidad = int(input(f"¿Cuántas unidades de '{producto['nombre']}'? "))
    except ValueError:
        print("La cantidad debe ser un número entero.")
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return

    # agregar al carrito o sumar si ya existe
    for item in carrito:
        if item["producto"]["id"] == id_input:
            item["cantidad"] += cantidad
            print(f"'{producto['nombre']}' ya estaba en el carrito. Cantidad actualizada a {item['cantidad']}.")
            return

    carrito.append({"producto": producto, "cantidad": cantidad})
    print(f"'{producto['nombre']}' x{cantidad} agregado al carrito.")


def mostrar_carrito_y_total(carrito):
    hacer_separador(50)
    
    if len(carrito) == 0:
        print("El carrito está vacío.")
        hacer_separador(50)
        return

    print(f"{'ID':<5} {'Nombre':<22} {'Cant.':>5} {'P. Unit':>10} {'Subtotal':>10}")
    hacer_separador(50)

    total = 0
    for item in carrito:
        p        = item["producto"]
        cantidad = item["cantidad"]
        subtotal = p["precio"] * cantidad
        total   += subtotal

        print(f"{p['id']:<5} {p['nombre']:<22} {cantidad:>5} ${p['precio']:>9} ${subtotal:>9}")

    hacer_separador(50)
    print(f"{'TOTAL A PAGAR:':>43} ${total:>9}")
    hacer_separador(50)


def vaciar_carrito(carrito):
    hacer_separador(35)

    if len(carrito) == 0:
        print("El carrito ya está vacío.")
        hacer_separador(35)
        return

    carrito.clear()
    print("El carrito ha sido vaciado.")
    hacer_separador(35)
            
def hacer_separador(cantidad):
    print("*" * cantidad)




# ejecución principal
while True:
    mostrar_menu()
    opcion = int(input("Ingrese la opción deseada: "))
    if (opcion==1):
        listar_productos()
    elif (opcion==2):
        buscar_producto(catalogo)
    elif (opcion==3):
        agregar_al_carrito(catalogo, carrito)
    elif (opcion==4):
        mostrar_carrito_y_total(carrito)
    elif (opcion==5):
        vaciar_carrito(carrito)
    elif (opcion==0):
        print("Saliendodoooodo")
        break
    else:
        print("opcion no válida...")