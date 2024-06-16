import pandas as pd


def read_csv():
    archivo = 'data/vgsales.csv'
   
    try: 
            df= pd.read_csv(archivo, sep=",")
            return df
    except FileNotFoundError as e:
            print("Error al ejecutar el archivo", e)
            return False
