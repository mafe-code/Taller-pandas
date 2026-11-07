import pandas as pd
from pathlib import Path

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    # 1. Que exista la columna "id_cliente" en ambos DataFrames
    if "id_cliente" not in clientes.columns or "id_cliente" not in ventas.columns:
        print("Falta la columna id_cliente en los datos.")
        return False

    # 2. Que "id_cliente" no esté repetido en clientes
    if clientes["id_cliente"].duplicated().any():
        print("Hay IDs duplicados en clientes.")
        return False

    # 3. Que tengan el mismo tipo de dato
    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print("Los tipos de id_cliente no coinciden.")
        return False

    # 4. Ver cuántas ventas no tienen cliente asociado (informativo)
    huerfanas = ~ventas["id_cliente"].isin(clientes["id_cliente"])
    print(f"Ventas sin cliente asociado: {huerfanas.sum()}")

    return True


def unir(clientes, ventas):
    # Validar primero
    if not validar_premerge(clientes, ventas):
        return None

    # Crear la carpeta procesada si no existe
    PROCESSED.mkdir(parents=True, exist_ok=True)

    # Hacer el merge tipo left join
    df_merged = pd.merge(ventas, clientes, on="id_cliente", how="left", validate="m:1")

    # Guardar en archivo CSV
    ruta_salida = PROCESSED / "merge.csv"
    df_merged.to_csv(ruta_salida, index=False)
    print("Merge guardado con éxito en Data/processed/merge.csv")

    return df_merged