
def stark_normalizar_datos(lista_heroes:list,campo:str,tipo_nuevo:str)->None:
    """Recorre la lista y convierte a otro tipo de dato las claves o keys 

    Args:
        lista_heroes (list): Lista de diccionario de los heroes\n
        campo (str): Campo o key del diccionario\n
        tipo_nuevo (str): Tipo a convertir el dato
    """
    
    datos_normalizados = False
    
    if len(lista_heroes) > 0:
        try:
            for heroe in lista_heroes:
                if type(heroe[campo]) != tipo_nuevo:
                    heroe[campo] = tipo_nuevo(heroe[campo])
                    datos_normalizados = True
        except ValueError:
            print("Error! Intentaste convertir a un tipo de dato que no se puede")
    else:
        print("Error! Lista de heroes vacia")
    
    if datos_normalizados:
        print("Datos normalizados")

def imprimir_dato(dato:str)->None:
    """Imprime un dato

    Args:
        dato (str): El dato a imprimir
    """
    print(dato)
