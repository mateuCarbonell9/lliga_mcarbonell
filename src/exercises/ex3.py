import os
import pandas as pd
import matplotlib.pyplot as plt
import config

def goals_distribution(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Calcula en cuántos partidos se marcó cada cantidad de goles (de local y de visitante).
    """
    # value_counts() cuenta frecuencias, sort_index() ordena de 0 goles en adelante
    home_counts = data['FTHG'].value_counts().sort_index()
    away_counts = data['FTAG'].value_counts().sort_index()
    
    # Convierto a DataFrames con el nombre de columna que pide el contexto
    distr_goals_home = pd.DataFrame(home_counts)
    distr_goals_home.columns = ['Partidos']
    distr_goals_home.index.name = 'Goles'
    
    distr_goals_away = pd.DataFrame(away_counts)
    distr_goals_away.columns = ['Partidos']
    distr_goals_away.index.name = 'Goles'
    
    return distr_goals_home, distr_goals_away

def plot_goals_ditribution(distr_goals_home: pd.DataFrame, distr_goals_away: pd.DataFrame) -> None:
    """
    Genera una figura con dos subplots para la distribución de goles.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Gráfica Local
    axes[0].bar(distr_goals_home.index, distr_goals_home['Partidos'], color='cornflowerblue')
    axes[0].set_title('Distribución de Goles - Local')
    axes[0].set_xlabel('Número de Goles')
    axes[0].set_ylabel('Número de Partidos')
    axes[0].set_xticks(distr_goals_home.index) # Fuerza a mostrar solo números enteros (0, 1, 2...)
    
    # Gráfica Visitante
    axes[1].bar(distr_goals_away.index, distr_goals_away['Partidos'], color='lightcoral')
    axes[1].set_title('Distribución de Goles - Visitante')
    axes[1].set_xlabel('Número de Goles')
    axes[1].set_ylabel('Número de Partidos')
    axes[1].set_xticks(distr_goals_away.index)
    
    plt.tight_layout()
    
    # Guardado de la imagen
    os.makedirs("src/img", exist_ok=True)
    filename = f"src/img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(filename)
    plt.close()