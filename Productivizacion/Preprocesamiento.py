# Fecha creacion: 26-06-23
# Autor: LMuroya
# Descripcion: Lee archivo, preprocesa y genera temporal en una ruta.

import pandas as pd
import os
import Utilidades as utils

ruta_in = 'Input'                               # Ruta donde se encuentra el archivo
ruta_tmp = 'Temp'                               # Ruta donde se guarda archivo intermedio
nombre_archivo = 'TelcoCustomerChurn_New.csv'   # Nombre del archivo input
nombre_temp = 'temp.csv'                        # Nombre del archivo temporal
sep = ';'                                       # Caracter de separación del archivo
index_col = 0                                   # Columna con el ID del cliente

root_path = os.getcwd()

## Lectura del archivo ##
os.chdir(ruta_in)
df_new = utils.leer_datos(nombre_archivo, sep, index_col)

# Ejecuta preprocesamiento si pudo leer correctamente el archivo
if df_new.shape[0]==0:
    print('No hay archivo leido')
else:
    print('Se leyó el dataframe')
    df_new.drop(columns = ['gender', 'MultipleLines', 'PhoneService', 'StreamingTV', 'StreamingMovies'], inplace = True)
    print('Se eliminaron columnas sobrantes')
    df_new = df_new.fillna(0)
    print('Se completaron vacíos potenciales con cero')
    
    # Variables binarias
    df_new['Partner']          = df_new['Partner'].map({'Yes':1,'No':0})
    df_new['Dependents']       = df_new['Dependents'].map({'Yes':1,'No':0})
    df_new['PaperlessBilling'] = df_new['PaperlessBilling'].map({'Yes':1,'No':0})

    # Variables ternarias
    df_new['InternetService']  = df_new['InternetService'].map({'Fiber optic':2, 'DSL':1, 'No':0})
    df_new['OnlineSecurity']   = df_new['OnlineSecurity'].map({'Yes':2, 'No':1, 'No internet service':0})
    df_new['OnlineBackup']     = df_new['OnlineBackup'].map({'Yes':2, 'No':1, 'No internet service':0})
    df_new['DeviceProtection'] = df_new['DeviceProtection'].map({'Yes':2, 'No':1, 'No internet service':0})
    df_new['TechSupport']      = df_new['TechSupport'].map({'Yes':2, 'No':1, 'No internet service':0})
    df_new['Contract']         = df_new['Contract'].map({'Month-to-month':2, 'Two year':1, 'One year':0})

    # Variables cuaternarias
    df_new['PaymentMethod']    = df_new['PaymentMethod'].map({'Electronic check':4, 'Mailed check':2, 'Bank transfer (automatic)':1, 'Credit card (automatic)':0})
    print('Se codificaron variables categoricas')

    os.chdir(root_path)
    os.chdir(ruta_tmp)
    df_new.reset_index().to_csv(nombre_temp, sep = sep, index = False)
    print('Se creo archivo intermedio. Fin del script.')



    
    