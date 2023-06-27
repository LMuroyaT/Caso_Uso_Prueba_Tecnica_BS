import pandas as pd
import os
import pickle
import Utilidades as utils
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings("ignore")

root_path = os.getcwd()             # Almacena la ruta raiz
model_path = 'Model'                # Carpeta con modelos serializados
model_file = 'random_forest.pckl'   # Archivo de modelo
temp_path  = 'Temp'                 # Carpeta con archivos temporales
temp_file  = 'temp.csv'             # Archivo temporal
out_path   = 'Output'               # Carpeta con salida del modelo
out_file   = 'Output_Fuga.csv'      # Archivo de salida
sep        = ';'                    # Caracter de separacion
index_col  = 0                      # Columna con ID de cliente para que sea indice

# Lectura del modelo
os.chdir(model_path)
with open(model_file,'rb') as file:
    model_prod = pickle.load(file)

# Lectura del temporal
os.chdir(root_path)
os.chdir(temp_path)

df_new = utils.leer_datos(temp_file, sep, index_col)

# Ejecuta preprocesamiento si pudo leer correctamente el archivo
if df_new.shape[0]==0:
    print('No hay archivo leido')
else:
    y_pred = model_prod.predict(df_new)
    y_proba = model_prod.predict_proba(df_new)[:,1]
    df_new['prediccion'] = y_pred
    df_new['probabilidad'] = y_proba
    print('Predicción realizada')
    df_new['decil'] = pd.cut(df_new['probabilidad'], bins = [-0.1,0.027665, 0.060643, 0.098030, 0.152734, 0.213479, 0.303149, 0.388618, 0.463306, 0.599900, 1.01], labels = [f'D{x}' for x in range(10,0,-1)])
    print('Deciles asignados')

    os.chdir(root_path)
    os.chdir(out_path)
    df_new.reset_index().to_csv(out_file, sep=';', index=False)
    print('Archivo de salida generado. Fin del proceso.')

