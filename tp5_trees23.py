from class_tree import BinaryTree

arbol_criaturas = BinaryTree()

criaturas = [
    {"name": "Ceto", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Tifón", "derrotado_por": "Zeus", "descripcion": "", "capturada": None},
    {"name": "Equidna", "derrotado_por": "Argos Panoptes", "descripcion": "", "capturada": None},
    {"name": "Dino", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Pefredo", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Enio", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Escila", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Caribdis", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Euríale", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Esteno", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Medusa", "derrotado_por": "Perseo", "descripcion": "", "capturada": None},
    {"name": "Ladón", "derrotado_por": "Heracles", "descripcion": "", "capturada": None},
    {"name": "Águila del Cáucaso", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Quimera", "derrotado_por": "Belerofonte", "descripcion": "", "capturada": None},
    {"name": "Hidra de Lerna", "derrotado_por": "Heracles", "descripcion": "", "capturada": None},
    {"name": "León de Nemea", "derrotado_por": "Heracles", "descripcion": "", "capturada": None},
    {"name": "Esfinge", "derrotado_por": "Edipo", "descripcion": "", "capturada": None},
    {"name": "Dragón de la Cólquida", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Cerbero", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Cerda de Cromión", "derrotado_por": "Teseo", "descripcion": "", "capturada": None},
    {"name": "Ortro", "derrotado_por": "Heracles", "descripcion": "", "capturada": None},
    {"name": "Toro de Creta", "derrotado_por": "Teseo", "descripcion": "", "capturada": None},
    {"name": "Jabalí de Calidón", "derrotado_por": "Atalanta", "descripcion": "", "capturada": None},
    {"name": "Carcinos", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Gerión", "derrotado_por": "Heracles", "descripcion": "", "capturada": None},
    {"name": "Cloto", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Láquesis", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Átropos", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Minotauro de Creta", "derrotado_por": "Teseo", "descripcion": "", "capturada": None},
    {"name": "Harpías", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Argos Panoptes", "derrotado_por": "Hermes", "descripcion": "", "capturada": None},
    {"name": "Aves del Estínfalo", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Talos", "derrotado_por": "Medea", "descripcion": "", "capturada": None},
    {"name": "Sirenas", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Pitón", "derrotado_por": "Apolo", "descripcion": "", "capturada": None},
    {"name": "Cierva de Cerinea", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Basilisco", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Jabalí de Erimanto", "derrotado_por": None, "descripcion": "", "capturada": None},
]


for c in criaturas:
    c["descripcion"] = ""
    c["capturada"] = None
    arbol_criaturas.insert(c["name"], c)

#A listado inorden de criaturas y quienes las derrotaron
print("criaturas y derrotadores:")
arbol_criaturas.in_order()
print()

#B cargar descripción (ejemplo)
talos = arbol_criaturas.search("Talos")
if talos:
    talos.other_values["descripcion"] = "Automata gigante de bronce"
    
#C mostrar información de Talos
print("información de Talos:")
if talos:
    print(talos.value, talos.other_values)
print()

#E listar criaturas derrotadas por Heracles
print("criaturas derrotadas por Heracles:")
def derrotadas_por(tree, heroe):
    def __rec(root):
        if root:
            __rec(root.left)
            if root.other_values["derrotado_por"] == heroe:
                print(root.value)
            __rec(root.right)
    if tree.root: __rec(tree.root)

derrotadas_por(arbol_criaturas, "Heracles")
print()

#F criaturas no derrotadas
print("criaturas no derrotadas:")
derrotadas_por(arbol_criaturas, None)
print()

#G modificar campo capturada
for name in ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabali de Erimanto"]:
    nodo = arbol_criaturas.search(name)
    if nodo:
        nodo.other_values["capturada"] = "Heracles"

#I búsqueda por coincidencia
print("buscando coincidencias con 'C':")
arbol_criaturas.proximity_search("C")
print()

#J eliminar Basilisco y Sirenas
arbol_criaturas.delete("Basilisco")
arbol_criaturas.delete("Sirenas")

#L modificar Ladón por Dragón Ladón
nodo_ladon = arbol_criaturas.search("ladon")
if nodo_ladon:
    datos = nodo_ladon.other_values
    arbol_criaturas.delete("Ladon")
    arbol_criaturas.insert("Dragón Ladon", datos)

#M listado por nivel
print("listado por nivel:")
arbol_criaturas.by_level()
print()

#N criaturas capturadas por Heracles
print("criaturas capturadas por Heracles:")
def capturadas_por(tree, heroe):
    def __rec(root):
        if root:
            __rec(root.left)
            if root.other_values["capturada"] == heroe:
                print(root.value)
            __rec(root.right)
    if tree.root: __rec(tree.root)

capturadas_por(arbol_criaturas, "Heracles")