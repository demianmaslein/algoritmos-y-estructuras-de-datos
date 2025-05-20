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
            
            
#carga de personajes
stack_personajes = Stack()
stack_personajes.push({'nombre': 'Iron Man', 'peliculas': 10})
stack_personajes.push({'nombre': 'Groot', 'peliculas': 4})
stack_personajes.push({'nombre': 'Capitan America', 'peliculas': 9})
stack_personajes.push({'nombre': 'Rocket Raccoon', 'peliculas': 5})
stack_personajes.push({'nombre': 'Doctor Strange', 'peliculas': 4})
stack_personajes.push({'nombre': 'Black Widow', 'peliculas': 7})
stack_personajes.push({'nombre': 'Gamora', 'peliculas': 4})


#A
def buscar_posiciones(stack):
    aux = Stack()
    posicion = 1
    posiciones_encontradas = {}

    while stack.size() > 0:
        personaje = stack.pop()
        nombre = personaje['nombre']
        if nombre == 'Rocket Raccoon' or nombre == 'Groot':
            posiciones_encontradas[nombre] = posicion
        aux.push(personaje)
        posicion += 1

    while aux.size() > 0:
        stack.push(aux.pop())

    for nombre in ['Rocket Raccoon', 'Groot']:
        if nombre in posiciones_encontradas:
            print(f"{nombre} está en la posición {posiciones_encontradas[nombre]} desde la cima.")
        else:
            print(f"{nombre} no se encuentra en la pila.")
            
#B
def personajes_mas_de_cinco(stack):
    aux = Stack()

    print("personajes con más de 5 películas:")
    while stack.size() > 0:
        personaje = stack.pop()
        if personaje['peliculas'] > 5:
            print(f"{personaje['nombre']}: {personaje['peliculas']} películas")
        aux.push(personaje)

    while aux.size() > 0:
        stack.push(aux.pop())
        
#C
def peliculas_black_widow(stack):
    aux = Stack()
    cantidad = 0

    while stack.size() > 0:
        personaje = stack.pop()
        if personaje['nombre'] == 'Black Widow':
            cantidad = personaje['peliculas']
        aux.push(personaje)

    while aux.size() > 0:
        stack.push(aux.pop())

    print(f"black Widow participó en {cantidad} películas.")

#D
def personajes_CDG(stack):
    aux = Stack()

    print("personajes cuyos nombres empiezan con C, D o G:")
    while stack.size() > 0:
        personaje = stack.pop()
        if personaje['nombre'].startswith(('C', 'D', 'G')):
            print("-", personaje['nombre'])
        aux.push(personaje)

    while aux.size() > 0:
        stack.push(aux.pop())
