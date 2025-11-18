from class_graph import Graph
from class_tree import BinaryTree


personajes = [
    {"nombre": "Luke Skywalker", "episodios": [4, 5, 6, 8, 9]},
    {"nombre": "Darth Vader", "episodios": [3, 4, 5, 6]},
    {"nombre": "Yoda", "episodios": [1, 2, 3, 5, 6, 8]},
    {"nombre": "Boba Fett", "episodios": [2, 5, 6]},
    {"nombre": "C-3PO", "episodios": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"nombre": "Leia", "episodios": [4, 5, 6, 7, 8, 9]},
    {"nombre": "Rey", "episodios": [7, 8, 9]},
    {"nombre": "Kylo Ren", "episodios": [7, 8, 9]},
    {"nombre": "Chewbacca", "episodios": [3, 4, 5, 6, 7, 8, 9]},
    {"nombre": "Han Solo", "episodios": [4, 5, 6, 7]},
    {"nombre": "R2-D2", "episodios": [1, 2, 3, 4, 5, 6, 7, 9]},
    {"nombre": "BB-8", "episodios": [7, 8, 9]},
]


g_sw = Graph(is_directed=False)


for p in personajes:
    g_sw.insert_vertex(p["nombre"])

def episodios_en_comun(lista1, lista2):
    return len(set(lista1).intersection(lista2))

for i in range(len(personajes)):
    for j in range(i + 1, len(personajes)):
        p1 = personajes[i]
        p2 = personajes[j]
        peso = episodios_en_comun(p1["episodios"], p2["episodios"])
        
        if peso > 0:
            g_sw.insert_edge(p1["nombre"], p2["nombre"], peso)
            g_sw.insert_edge(p2["nombre"], p1["nombre"], peso)


#hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
print("MST desde C-3PO")
g_sw.minimal_spanning_tree("C-3PO")

print("MST desde Yoda")
g_sw.minimal_spanning_tree("Yoda")

print("MST desde Leia")
g_sw.minimal_spanning_tree("Leia")

#determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
maximo = 0
pares = []

for v in g_sw.elements:
    for ady in g_sw.get_adjacent(v):
        peso = ady['peso']
        destino = ady['vertex']

        if peso > maximo:
            maximo = peso
            pares = [(v, destino)]
        elif peso == maximo:
            pares.append((v, destino))

print("Máximo de episodios:", maximo)
print("Pares con ese máximo:")
for p in pares:
    print(p)

#calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
camino1 = g_sw.shortest_path("C-3PO", "R2-D2")
print("camino más corto C-3PO → R2-D2:", camino1)

camino2 = g_sw.shortest_path("Yoda", "Darth Vader")
print("camino más corto Yoda → Darth Vader:", camino2)

#indicar qué personajes aparecieron en los nueve episodios de la saga.
print("personajes presentes en los 9 episodios:")

for p in personajes:
    if len(p["episodios"]) == 9:
        print(p["nombre"])

