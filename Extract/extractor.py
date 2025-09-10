import pandas as pd
import os

class Extractor:
    def __init__(self, input_path):
        self.input_path = input_path

    def extract(self):
        if not os.path.exists(self.input_path):
            print(f"El archivo {self.input_path} no existe.")
            return None
        try:
            df = pd.read_csv(self.input_path, low_memory=False)
            print(f"Archivo cargado con {df.shape[0]} filas y {df.shape[1]} columnas.")
            return df
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None
