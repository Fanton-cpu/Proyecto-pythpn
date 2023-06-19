def length(l):
    metering = {  # Medidas
        'standard lenght': l['Lenght1'], # Longitud estandar
        'fork lenght': l['Lenght2'],     # Longitud horquidea
        'total length': l['Length3']     # Longitud total
    }
    labels = list(metering.keys())      #Etiqueta 
    values = list(metering.values())    #Valores
    return labels, values