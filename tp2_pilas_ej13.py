from typing import Any, Optional

class Stack:

    def __init__(self):
        self.__elements = []


    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())


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

    while stack.size() > 0:
        traje = stack.pop()
        if traje['modelo'] == 'Mark XLIV':
            peliculas.append(traje['pelicula'])
        aux.push(traje)

    while aux.size() > 0:
        stack.push(aux.pop())

    if peliculas:
        print("el modelo Mark XLIV (Hulkbuster) fue utilizado en las películas:")
        for pelicula in peliculas:
            print("-", pelicula)
    else:
        print("el modelo Mark XLIV no fue utilizado en ninguna película.")


#B
def mostrar_modelos_dañados(stack):
    aux = Stack()
    modelos_dañados = []

    while stack.size() > 0:
        traje = stack.pop()
        if traje["estado"].lower() == "dañado":
            modelos_dañados.append(traje["modelo"])
        aux.push(traje)

    while aux.size() > 0:
        stack.push(aux.pop())

    if modelos_dañados:
        print("modelos dañados encontrados:")
        for modelo in set(modelos_dañados):
            print("-", modelo)
    else:
        print("no hay modelos dañados")


#C
def eliminar_modelos_destruidos(stack):
    aux = Stack()
    print("modelos destruidos eliminados:")

    while stack.size() > 0:
        traje = stack.pop()
        if traje["estado"].lower() == "destruido":
            print("-", traje["modelo"])
          
        else:
            aux.push(traje)

    while aux.size() > 0:
        stack.push(aux.pop())


#E
def agregar_traje_si_no_existe(stack):
    modelo_nuevo = "Mark LXXXV"
    pelicula_nueva = "Avengers: Endgame"
    estado_nuevo = "Impecable"

    existe = False
    aux = Stack()

    while stack.size() > 0:
        traje = stack.pop()
        if traje["modelo"] == modelo_nuevo and traje["pelicula"] == pelicula_nueva:
            existe = True
        aux.push(traje)

    while aux.size() > 0:
        stack.push(aux.pop())

    if not existe:
        stack.push({
            "modelo": modelo_nuevo,
            "pelicula": pelicula_nueva,
            "estado": estado_nuevo
        })
        print(f"se agregó el modelo {modelo_nuevo} a la película {pelicula_nueva}.")
    else:
        print(f"el modelo {modelo_nuevo} ya estaba cargado para la película {pelicula_nueva}. No se agregó.")


#F
def mostrar_trajes_por_pelicula(stack):
    aux = Stack()
    trajes_homecoming = []
    trajes_civilwar = []

    while stack.size() > 0:
        traje = stack.pop()
        if traje["pelicula"] == "Spider-Man: Homecoming":
            trajes_homecoming.append(traje["modelo"])
        elif traje["pelicula"] == "Capitan America: Civil War":
            trajes_civilwar.append(traje["modelo"])
        aux.push(traje)

    while aux.size() > 0:
        stack.push(aux.pop())

    if trajes_homecoming:
        print("trajes utilizados en Spider-Man: Homecoming:")
        for modelo in set(trajes_homecoming):
            print("-", modelo)
    else:
        print("no se encontraron trajes en Spider-Man: Homecoming.")

    if trajes_civilwar:
        print("trajes utilizados en Capitan America: Civil War:")
        for modelo in set(trajes_civilwar):
            print("-", modelo)
    else:
        print("no se encontraron trajes en Capitan America: Civil War.")