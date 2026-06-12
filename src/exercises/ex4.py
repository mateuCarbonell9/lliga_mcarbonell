import os
import pandas as pd
import matplotlib.pyplot as plt
import config

def FTR(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el número de partidos ganados por locales (H), visitantes (A) o partidos empatados (D).
    """
    # Se cuenta la frecuencia de cada valor en la columna 'FTR' (Full Time Result)
    counts = data['FTR'].value_counts()
    
    # Lo convertimos a DataFrame y renombramos columnas para mayor claridad
    df_ftr = pd.DataFrame(counts).reset_index()
    df_ftr.columns = ['Result', 'Matches']
    
    return df_ftr

def plot_FTR(ftr: pd.DataFrame) -> None:
    """
    Genera un diagrama de barras con los resultados de los partidos.
    """
    plt.figure(figsize=(8, 5))
    
    # Asignamos colores representativos: Verde (Gana Local), Rojo (Gana Visitante), Gris (Empate)
    colores = ['mediumseagreen', 'indianred', 'lightgray']
    
    plt.bar(ftr['Result'], ftr['Matches'], color=colores)
    
    plt.title('Resultados de Partidos (H: Local, A: Visitante, D: Empate)')
    plt.xlabel('Resultado')
    plt.ylabel('Número de Partidos')
    
    plt.tight_layout()
    
    # Guardado de la imagen
    os.makedirs("src/img", exist_ok=True)
    filename = f"src/img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(filename)
    plt.close()