#5. Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_decimal(nromano) :
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}   
    
    if len(nromano) == 0:
        return 0
    elif len(nromano) == 1:
        return valores[nromano]
    else: 
        if valores[nromano[0]] >= valores[nromano[1]]:
            return valores[nromano[0]] + romano_decimal(nromano[1:])
        else:
            return -valores[nromano[0]] + romano_decimal(nromano[1:]) 
        
        

        