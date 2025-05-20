class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


#carga de los trajes
stack_trajes = Stack()
stack_trajes.push({'modelo': 'Mark III', 'pelicula': 'Iron Man', 'estado': 'Dañado'})
stack_trajes.push({'modelo': 'Mark V', 'pelicula': 'Iron Man 2', 'estado': 'Destruido'})
stack_trajes.push({'modelo': 'Mark XLII', 'pelicula': 'Iron Man 3', 'estado': 'Destruido'})
stack_trajes.push({'modelo': 'Mark XLIV', 'pelicula': 'Avengers: Age of Ultron', 'estado': 'Dañado'})
stack_trajes.push({'modelo': 'Mark XLVI', 'pelicula': 'Capitan America: Civil War', 'estado': 'Impecable'})
stack_trajes.push({'modelo': 'Mark XLVII', 'pelicula': 'Spider-Man: Homecoming', 'estado': 'Dañado'})
stack_trajes.push({'modelo': 'Mark LXXXV', 'pelicula': 'Avengers: Endgame', 'estado': 'Destruido'})


#A
def buscar_hulkbuster(stack):
    aux = Stack()
    peliculas = []

    while not stack.is_empty():
        traje = stack.pop()
        if traje['modelo'] == 'Mark XLIV':
            peliculas.append(traje['pelicula'])
        aux.push(traje)

    while not aux.is_empty():
        stack.push(aux.pop())

    if peliculas:
        print("El modelo Mark XLIV (Hulkbuster) fue utilizado en las películas:")
        for pelicula in peliculas:
            print("-", pelicula)
    else:
        print("El modelo Mark XLIV no fue utilizado en ninguna película.")


#B
def mostrar_modelos_dañados(stack):
    aux = Stack()
    modelos_dañados = []

    while not stack.is_empty():
        traje = stack.pop()
        if traje["estado"].lower() == "dañado":
            modelos_dañados.append(traje["modelo"])
        aux.push(traje)

    while not aux.is_empty():
        stack.push(aux.pop())

    if modelos_dañados:
        print("Modelos dañados encontrados:")
        for modelo in set(modelos_dañados):
            print("-", modelo)
    else:
        print("No hay modelos dañados")


#C
def eliminar_modelos_destruidos(stack):
    aux = Stack()
    print("Modelos destruidos eliminados:")

    while not stack.is_empty():
        traje = stack.pop()
        if traje["estado"].lower() == "destruido":
            print("-", traje["modelo"])
          
        else:
            aux.push(traje)

    while not aux.is_empty():
        stack.push(aux.pop())


#E
def agregar_traje_si_no_existe(stack):
    modelo_nuevo = "Mark LXXXV"
    pelicula_nueva = "Avengers: Endgame"
    estado_nuevo = "Impecable"

    existe = False
    aux = Stack()

    while not stack.is_empty():
        traje = stack.pop()
        if traje["modelo"] == modelo_nuevo and traje["pelicula"] == pelicula_nueva:
            existe = True
        aux.push(traje)

    while not aux.is_empty():
        stack.push(aux.pop())

    if not existe:
        stack.push({
            "modelo": modelo_nuevo,
            "pelicula": pelicula_nueva,
            "estado": estado_nuevo
        })
        print(f"Se agregó el modelo {modelo_nuevo} a la película {pelicula_nueva}.")
    else:
        print(f"El modelo {modelo_nuevo} ya estaba cargado para la película {pelicula_nueva}. No se agregó.")


#F
def mostrar_trajes_por_pelicula(stack):
    aux = Stack()
    trajes_homecoming = []
    trajes_civilwar = []

    while not stack.is_empty():
        traje = stack.pop()
        if traje["pelicula"] == "Spider-Man: Homecoming":
            trajes_homecoming.append(traje["modelo"])
        elif traje["pelicula"] == "Capitan America: Civil War":
            trajes_civilwar.append(traje["modelo"])
        aux.push(traje)

    while not aux.is_empty():
        stack.push(aux.pop())

    if trajes_homecoming:
        print("Trajes utilizados en Spider-Man: Homecoming:")
        for modelo in set(trajes_homecoming):
            print("-", modelo)
    else:
        print("No se encontraron trajes en Spider-Man: Homecoming.")

    if trajes_civilwar:
        print("\nTrajes utilizados en Capitan America: Civil War:")
        for modelo in set(trajes_civilwar):
            print("-", modelo)
    else:
        print("No se encontraron trajes en Capitan America: Civil War.")