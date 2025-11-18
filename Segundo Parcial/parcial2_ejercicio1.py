from class_tree import BinaryTree
from pokemons_data import pokemons  






arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()


def insertar_en_arbol_nombre(p):
    arbol_nombre.insert(p["nombre"], p)

def insertar_en_arbol_numero(p):
    arbol_numero.insert(p["numero"], p)

def insertar_en_arbol_tipo(p):
    for tipo in p["tipos"]:
        nodo = arbol_tipo.search(tipo)

        if nodo is None:
            arbol_tipo.insert(tipo, [p])
        else:          
            nodo.other_values.append(p)


for p in pokemons:
    insertar_en_arbol_nombre(p)
    insertar_en_arbol_numero(p)
    insertar_en_arbol_tipo(p)

#mostrar todos los datos de un Pokémon a partir de su número y nombre
def buscar_por_numero(numero):
    nodo = arbol_numero.search(numero)
    if nodo:
        print(nodo.other_values)
    else:
        print("No existe ese número en la Pokédex.")

def buscar_por_nombre_proximidad(prefijo):
    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            if prefijo.lower() in root.value.lower():
                print(root.other_values)
            recorrer(root.right)

    recorrer(arbol_nombre.root)

#mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
def mostrar_por_tipo(tipo):
    nodo = arbol_tipo.search(tipo)
    if nodo is None:
        print(f"No hay pokémon de tipo {tipo}")
    else:
        for p in nodo.other_values:
            print(p["nombre"])

#realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
print("Pokémon ordenados por número:")
arbol_numero.in_order()

print("Pokémon ordenados por nombre:")
arbol_nombre.in_order()

print("Listado por nivel (nombre):")
arbol_nombre.by_level()

#mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
def pokemons_debiles_a(nombre):
    nodo = arbol_nombre.search(nombre)
    if nodo is None:
        return []

    tipos_ataque = nodo.other_values["tipos"]
    resultado = []

    def recorrer(root):
        if root:
            recorrer(root.left)
            p = root.other_values
            # Si comparte tipo con las debilidades del pokémon que atacaría
            if any(t in p["debilidad"] for t in tipos_ataque):
                resultado.append(p["nombre"])
            recorrer(root.right)

    recorrer(arbol_nombre.root)
    return resultado

#mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
def contar_por_tipo():
    def recorrer(root):
        if root:
            recorrer(root.left)
            print(root.value, "→", len(root.other_values))
            recorrer(root.right)

    recorrer(arbol_tipo.root)

#determinar cuantos Pokémons tienen megaevolucion.
def contar_mega():
    total = 0
    def recorrer(root):
        nonlocal total
        if root:
            recorrer(root.left)
            if root.other_values["mega"] is True:
                total += 1
            recorrer(root.right)

    recorrer(arbol_nombre.root)
    return total

#determinar cuantos Pokémons tiene forma gigamax.
def contar_gigamax():
    total = 0
    def recorrer(root):
        nonlocal total
        if root:
            recorrer(root.left)
            if root.other_values["giga"] is True:
                total += 1
            recorrer(root.right)

    recorrer(arbol_nombre.root)
    return total



