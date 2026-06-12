"""
Módulo para el Ejercicio 1: Carga de dataset, EDA y visualización de goles.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import config  

def load_and_eda(file_path: str) -> pd.DataFrame:
    """
    Carga el dataset de La Liga, elimina columnas innecesarias el DataFrame resultante.
    
    file_path: Ruta relativa del archivo CSV.
    Devuelve el DataFrame de Pandas con los datos limpios.
    """
    # Carga del dataset usando la ruta relativa
    df = pd.read_csv(file_path)
    
    # Elimino las columnas que se pide
    columns_to_drop = ["HTHG", "HTAG", "HTR"]
    df = df.drop(columns=columns_to_drop, errors='ignore')
    
    return df

def plot_home_away_goals(data: pd.DataFrame) -> None:
    """
    Genera y guarda un plot con la distribución de goles en casa y fuera.
    
    DataFrame con los datos de los partidos.
    """
    # Creo una figura con dos subplots uno al lado del otro
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # Gráfica para goles en casa (FTHG)
    axes[0].boxplot(data['FTHG'].dropna())
    axes[0].set_title('Goles Equipo Local (Home)')
    axes[0].set_ylabel('Número de Goles')
    
    # Gráfica para goles fuera (FTAG)
    axes[1].boxplot(data['FTAG'].dropna())
    axes[1].set_title('Goles Equipo Visitante (Away)')
    axes[1].set_ylabel('Número de Goles')
    
    plt.tight_layout()
    
    os.makedirs("src/img", exist_ok=True)
    filename = f"src/img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(filename)
    plt.close()  