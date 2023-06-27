# Fecha creacion: 26-06-23
# Autor: LMuroya
# Descripcion: Contiene funciones de utilidades para ser reusadas.

import pandas as pd

def leer_datos(nombre_archivo, sep = ',', index_col = 0):
    try:
        df = pd.read_csv(nombre_archivo, sep = sep, index_col = index_col)
    except:
        df = pd.DataFrame()
        print('No se pudo leer el archivo')
    finally:
        return df