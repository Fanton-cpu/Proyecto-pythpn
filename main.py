import pandas as pd
from utils import length
import charts

def run():
    # Leer el archivo CSV y cargar los datos en un DataFrame
    df = pd.read_csv('data/Fish.csv')

    # Obtener las etiquetas y los valores utilizando la función length()
    labels, values = length(df)

    # Llamar a la función en charts.py para generar las gráficas
    charts.generate_bar_chart(labels, values)

if __name__ == "__main__":
    run()