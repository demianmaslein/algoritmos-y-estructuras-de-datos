from class_tree import BinaryTree 
from class_queue import Queue  

arbol = BinaryTree()

personajes = [
    {"name": "Iron Man", "is_villain": False},
    {"name": "Thanos", "is_villain": True},
    {"name": "Capitán América", "is_villain": False},
    {"name": "Red Skull", "is_villain": True},
    {"name": "Hulk", "is_villain": False},
    {"name": "Black Widow", "is_villain": False},
    {"name": "Ultron", "is_villain": True},
    {"name": "Doctor Strnge", "is_villain": False},  # mal cargado
    {"name": "Loki", "is_villain": True},
    {"name": "Spider-Man", "is_villain": False},
    {"name": "Black Panther", "is_villain": False},
    {"name": "Hela", "is_villain": True},
    {"name": "Scarlet Witch", "is_villain": False},
    {"name": "Captain Marvel", "is_villain": False},
    {"name": "Vision", "is_villain": False},
]

for p in personajes:
    arbol.insert(p["name"], p)

#B listar los villanos ordenados alfabéticamente;
print("villanos ordenados alfabeticamente:")
arbol.villain_in_order()

#C mostrar todos los superhéroes que empiezan con C;
print("superheroes que empiezan con 'C':")
arbol.proximity_search('C')

#D determinar cuántos superhéroes hay el árbol;
print("Cantidad de superheroes en el árbol:")
print(arbol.count_heroes())

#E Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
print("corrigiendo el nombre de Doctor Strnge")

arbol.proximity_search('Dr')

valor, otros_valores = arbol.delete('Doctor Strnge')
if valor is not None:
    otros_valores['name'] = 'Doctor Strange'
    arbol.insert('Doctor Strange', otros_valores)

print("Verificación:")
arbol.proximity_search('Dr')

#F listar los superhéroes ordenados de manera descendente;
def in_order_descendente(root):
    if root is not None:
        in_order_descendente(root.right)
        if root.other_values["is_villain"] is False:
            print(root.value)
        in_order_descendente(root.left)

print("superheroes ordenados de forma descendente:")
in_order_descendente(arbol.root)

#G
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

arbol.divide_tree(arbol_heroes, arbol_villanos)

#I determinar cuántos nodos tiene cada árbol;
print("cantidad de héroes:", arbol_heroes.count_heroes())
def contar_villanos(root):
    if root is None:
        return 0
    count = 0
    if root.other_values["is_villain"] is True:
        count += 1
    count += contar_villanos(root.left)
    count += contar_villanos(root.right)
    return count

print("cantidad de villanos:", contar_villanos(arbol_villanos.root))

#II realizar un barrido ordenado alfabéticamente de cada árbol.
print("heroes ordenados alfabéticamente:")
arbol_heroes.in_order()

print("villanos ordenados alfabéticamente:")
arbol_villanos.in_order()




