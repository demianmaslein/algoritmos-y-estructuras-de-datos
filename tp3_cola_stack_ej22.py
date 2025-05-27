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
            

class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]:
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]:
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
    
    def show(self):
        for i in range(len(self.__elements)):
            print(self.move_to_end())
            
            
            
 #ej 22 cola y stack           

cola_personajes = Queue()
cola_personajes.arrive({'personaje': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'})
cola_personajes.arrive({'personaje': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'})
cola_personajes.arrive({'personaje': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'})
cola_personajes.arrive({'personaje': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'})
cola_personajes.arrive({'personaje': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'})
cola_personajes.arrive({'personaje': 'Stephen Strange', 'superheroe': 'Doctor Strange', 'genero': 'M'})
cola_personajes.arrive({'personaje': 'Gamora', 'superheroe': 'Gamora', 'genero': 'F'})


aux = Queue()

print("el nombre del personaje de la superhéroe Capitana Marvel es: ")
while cola_personajes.size() > 0:
    dato = cola_personajes.attention()
    
    if dato['superheroe'] == 'Capitana Marvel':
        print("-", dato['personaje'])

    if dato['genero'] == 'F':
        pass  

    aux.arrive(dato)


print("nombres de los superhéroes femeninos: ")
while aux.size() > 0:
    dato = aux.attention()

    if dato['genero'] == 'F':
        print("-", dato['superheroe'])

    aux.arrive(dato)

print("nombres de los superheroes masculinos: ")
for _ in range(aux.size()):
    dato = aux.attention()

    if dato['genero'] == 'M':
        print("-", dato['personaje'])

    aux.arrive(dato)

print("superhéroe del personaje Scott Lang: ")
for _ in range(aux.size()):
    dato = aux.attention()

    if dato['personaje'] == 'Scott Lang':
        print("-", dato['superheroe'])

    aux.arrive(dato)

print("personajes o superhéroes que comienzan con la letra S:")
for _ in range(aux.size()):
    dato = aux.attention()

    if dato['personaje'].startswith('S') or dato['superheroe'].startswith('S'):
        print("-", dato)

    aux.arrive(dato)

print("Carol Danvers está en la cola?")
encontrado = False
for _ in range(aux.size()):
    dato = aux.attention()

    if dato['personaje'] == 'Carol Danvers':
        print("Carol Danvers está en la cola como:", dato['superheroe'])
        encontrado = True

    aux.arrive(dato)

if not encontrado:
    print("Carol Danvers no está en la cola.")
