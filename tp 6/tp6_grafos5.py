from class_graph import Graph

# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-dor, router, switch, impresora;

g = Graph(is_directed=False)

equipos = [
    ("Red Hat", "notebook"),
    ("Debian", "notebook"),
    ("Arch", "notebook"),

    ("Manjaro", "pc"),
    ("Parrot", "pc"),
    ("Fedora", "pc"),
    ("Ubuntu", "pc"),
    ("Mint", "pc"),

    ("Guarani", "servidor"),
    ("MongoDB", "servidor"),

    ("Switch 1", "switch"),
    ("Switch 2", "switch"),

    ("Router 1", "router"),
    ("Router 2", "router"),
    ("Router 3", "router"),

    ("Impresora", "impresora")
]

for nombre, tipo in equipos:
    g.insert_vertex(nombre, other_value={"tipo": tipo})

# conexiones (aristas)

conexiones = [
    ("Red Hat", "Router 2", 25),
    ("Debian", "Switch 1", 17),
    ("Ubuntu", "Switch 1", 18),
    ("Impresora", "Switch 1", 22),
    ("Mint", "Switch 1", 80),
    ("Switch 1", "Router 1", 29),
    ("Router 1", "Router 2", 37),
    ("Router 1", "Router 3", 43),
    ("Router 2", "Guarani", 9),
    ("Router 2", "Router 3", 50),
    ("Router 3", "Switch 2", 61),
    ("Switch 2", "Manjaro", 40),
    ("Switch 2", "Parrot", 12),
    ("Switch 2", "Fedora", 3),
    ("Switch 2", "Arch", 56),
    ("Switch 2", "MongoDB", 5)
]

for a, b, w in conexiones:
    g.insert_edge(a, b, w)
    g.insert_edge(b, a, w)

print("Grafo cargado correctamente.\n")

#b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;

notebooks = ["Red Hat", "Debian", "Arch"]

print("Barrido en profundidad:")
for nb in notebooks:
    print(f"DFS desde {nb}:")
    g.deep_sweep(nb)
    print()

print("Barrido en amplitud:")
for nb in notebooks:
    print(f"BFS desde {nb}:")
    g.amplitude_sweep(nb)
    print()

#c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;

print("Caminos más cortos hacia la impresora:\n")

pc_origenes = ["Manjaro", "Red Hat", "Fedora"]

for pc in pc_origenes:
    ruta = g.shortest_path(pc, "Impresora")
    print(f"{pc} → Impresora: {ruta}")

print()

#d. encontrar el árbol de expansión mínima;

print("Árbol de expansión mínima (Kruskal):")
mst = g.kruskal()
print(mst, "\n")

#e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;

pcs = ["Manjaro", "Parrot", "Fedora", "Ubuntu", "Mint"]

mejor_pc = None
mejor_costo = float("inf")
mejor_camino = None

for pc in pcs:
    camino = g.shortest_path(pc, "Guarani")
    if camino and camino[-1][1] < mejor_costo:
        mejor_pc = pc
        mejor_costo = camino[-1][1]
        mejor_camino = camino

print("PC más cercana a Guaraní:")
print(f"{mejor_pc} con costo {mejor_costo}")
print(f"camino: {mejor_camino}\n")

#f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;

vecinos_sw1 = [v["vertex"] for v in g.get_adjacent("Switch 1")]
computadoras_sw1 = [v for v in vecinos_sw1 if v in ["Ubuntu", "Mint", "Debian"]]

mejor_equipo = None
mejor_costo = float("inf")
mejor_camino = None

for pc in computadoras_sw1:
    camino = g.shortest_path(pc, "MongoDB")
    if camino and camino[-1][1] < mejor_costo:
        mejor_equipo = pc
        mejor_costo = camino[-1][1]
        mejor_camino = camino

print("computadora del Switch 1 más cercana a MongoDB:")
print(f"{mejor_equipo} con costo {mejor_costo}")
print(f"camino: {mejor_camino}\n")

# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;

print("modificando conexión de la impresora")

g.delete_edge("impresora", "switch 1", "value")
g.delete_edge("switch 1", "impresora", "value")

g.insert_edge("impresora", "router 2", 22)
g.insert_edge("router 2", "impresora", 22)

print("barridos tras modificar conexión:\n")

print("DFS:")
for nb in notebooks:
    print(f"DFS desde {nb}:")
    g.deep_sweep(nb)
    print()

print("BFS:")
for nb in notebooks:
    print(f"BFS desde {nb}:")
    g.amplitude_sweep(nb)
    print()