# def perimetro_cuadrado(lado):
#     perimetro=lado*4
#     return perimetro 
    # return perimetro  ==> si una funcion no tiene un return estaria volviendo un valor NONE


def calcular_cuadrado(lado):
    perimetro=lado*4
    area=lado*lado
    return area,perimetro 

# def area_cuadrado(lado):
#     area=lado*lado
#     return area

# perimetro=perimetro_cuadrado(lado=5)
# area=area_cuadrado(lado=5)
# print(f"area:{area},Perimatro:{perimetro}")

resultado=calcular_cuadrado(lado=5)
print(resultado)#de esta manera se retornan dos valores y ademas los devulve en una tupla