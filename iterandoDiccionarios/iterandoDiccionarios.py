marcas={
    "ford":"alemana",
    "fiat":"italiana"
}

for llave in marcas:
    print("llave:",llave)
    """essto mostrara ford,fiat"""
    print("valor",marcas[llave])
    """essto mostrara alemana,ialiana"""



for elemento in marcas.keys():
    print(elemento)
    #esto solo mostrar ford y fiat que son las keys()

    
for elemento in marcas.values():
    print(elemento)
    #esto solo mostrar alemana,italiana que son los valores de values()

for llave,valor in marcas.items():
        print(llave,valor)

#esto me mostra tanto la propiedad o key como su valor gracias a la funcion items()