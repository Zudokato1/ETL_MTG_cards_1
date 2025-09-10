from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader

def main():
    # 1. Extraer datos
    extractor = Extractor(Config.INPUT_PATH)
    df = extractor.extract()
    if df is None:
        return

    # 2. Transformar datos
    transformer = Transformer(df)
    clean_df = transformer.select_columns()

    # 3. Cargar datos
    loader = Loader(clean_df, Config.OUTPUT_PATH, Config.DB_PATH)
    loader.save_to_csv()
    loader.save_to_sqlite()

if __name__ == "__main__":
    main()
