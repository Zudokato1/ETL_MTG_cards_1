class Transformer:
    def __init__(self, dataframe):
        self.df = dataframe

    def select_columns(self):
        columnas = ["name", "colors", "rarity"]
        df_clean = self.df[columnas].copy()
        print(f"Transformación completada. Quedan {df_clean.shape[1]} columnas y {df_clean.shape[0]} filas.")
        return df_clean
