from class_graph import Graph

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
g_casa = Graph(is_directed=False)

ambientes = [
    "cocina", "comedor", "cochera", "quincho",
    "baño 1", "baño 2", "habitación 1", "habitación 2",
    "sala de estar", "terraza", "patio"
]

for a in ambientes:
    g_casa.insert_vertex(a)

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;

conexiones = [
    ("cocina", "comedor", 4),
    ("cocina", "patio", 6),
    ("cocina", "baño 1", 5),

    ("comedor", "sala de estar", 3),
    ("comedor", "terraza", 8),
    ("comedor", "habitacion 1", 7),

    ("cochera", "quincho", 10),
    ("cochera", "patio", 12),
    ("cochera", "baño 2", 9),

    # quincho: 5 conexiones
    ("quincho", "patio", 4),
    ("quincho", "terraza", 13),
    ("quincho", "sala de estar", 11),
    ("quincho", "habitacion 2", 15),

    ("baño 1", "habitacion 1", 6),
    ("baño 1", "baño 2", 3),

    ("baño 2", "habitacion 2", 5),
    ("baño 2", "sala de estar", 9),

    ("habitacion 1", "habitacion 2", 4),
    ("habitacion 1", "sala de estar", 7),

    ("habitacion 2", "terraza", 6),

    # sala de estar: 5 conexiones
    ("sala de estar", "terraza", 5),
    ("sala de estar", "patio", 9),

    ("terraza", "patio", 10),
]

for a, b, d in conexiones:
    g_casa.insert_edge(a, b, d)
    g_casa.insert_edge(b, a, d)  

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
print("arbol de expansión mínima de la casa:")
mst = g_casa.minimal_spanning_tree("cocina") 

total_metros = sum(edge["peso"] for edge in mst)

print("metros totales de cable necesarios:", total_metros, "m")

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
camino = g_casa.shortest_path("habitación 1", "sala de estar")
print("camino más corto habitación 1 → sala de estar:")
print(camino)