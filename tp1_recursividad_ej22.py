#Ejercicio 22


def usar_la_fuerza (mochila):
    if len(mochila) == 0 :
        return -1
    elif mochila[0] != "sable" : 
        return 1 + usar_la_fuerza(mochila[1:])
    else:
        mochila[0] == "sable" 
        return 0
    