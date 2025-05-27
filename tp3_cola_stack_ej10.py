
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
            
            
            
            
            
#ej 10 cola y stack          
            
def eliminar_facebook(queue: Queue):
    aux = Queue()
    while queue.size() > 0:
        notificacion = queue.attention()
        if notificacion['app'] != 'facebook':
            aux.arrive(notificacion)
    while aux.size() > 0:
        queue.arrive(aux.attention())

def mostrar_twitter_python(queue: Queue):
    aux = Queue()
    print("notificaciones de twitter con python: ")
    while queue.size() > 0:
        notificacion = queue.attention()
        if notificacion['app'] == 'twitter' and 'python' in notificacion['mensaje']:
            print(notificacion)
        aux.arrive(notificacion)
    while aux.size() > 0:
        queue.arrive(aux.attention())

def contar_notificaciones_hora(queue: Queue):
    stack = Stack()
    contador = 0
    while queue.size() > 0:
        notificacion = queue.attention()
        hora = notificacion['hora']
        if '11:43' <= hora <= '15:57':
            stack.push(notificacion)
            count += 1
        queue.arrive(notificacion)
    print(f"Cantidad de notificaciones entre 11:43 y 15:57: {contador}")
    return stack                  