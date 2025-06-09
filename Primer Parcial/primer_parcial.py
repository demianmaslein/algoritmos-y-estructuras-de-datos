
lista_superh= [
    "Iron Man"
    "Capitan America"
    "Black Widow"
    "Hulk"
    "Hawkeye"
    "Thor"
    "Spider Man"
    "Groot"
    "Ant Man"
    "Black Panther"
    "Doctor Strange"
    "Capitana Marvel"
    "Vision"
    "Scarlet Witch"
    "Falcon" 
    ]

def buscar_capamerica(lista_superh, i=0):
    if i >= len(lista_superh):
        return "no se encuentra en la lista"
    if lista_superh[i] == "Capitan America":
        return lista_superh[i]
    return buscar_capamerica(lista_superh, i + 1)


def listar_superheroes(lista_superh, i=0):
    if i >= len(lista_superh):
        return
    print(lista_superh[i])
    listar_superheroes(lista_superh, i + 1)
