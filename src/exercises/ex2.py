import os
import pandas as pd
import matplotlib.pyplot as plt
import config

def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el número total de partidos jugados por cada equipo.
    """
    # Contamos las veces que cada equipo juega en casa y fuera
    home_matches = data['HomeTeam'].value_counts()
    away_matches = data['AwayTeam'].value_counts()
    
    # Sumamos ambas cantidades
    total = home_matches.add(away_matches, fill_value=0).astype(int)
    
    # Ordenamos de mayor a menor y lo convertimos a DataFrame
    total = total.sort_values(ascending=False)
    df_total = total.reset_index()
    df_total.columns = ['Team', 'Total_Matches']
    
    return df_total

def plot_matches_team_total(matches_team_total: pd.DataFrame) -> None:
    """
    Muestra el total de partidos por equipo en un diagrama de barras.
    """
    plt.figure(figsize=(12, 5))
    
    # Diagrama de barras básico
    plt.bar(matches_team_total['Team'], matches_team_total['Total_Matches'])
    
    plt.title('Total de partidos jugados por equipo')
    plt.xlabel('Equipos')
    plt.ylabel('Número de partidos')
    
    # Rotamos los nombres para que se puedan leer
    plt.xticks(rotation=90, fontsize=8)
    plt.tight_layout()
    
    # Guardamos en la misma carpeta que el ejercicio 1
    os.makedirs("src/img", exist_ok=True)
    filename = f"src/img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(filename)
    plt.close()