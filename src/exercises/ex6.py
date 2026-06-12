import os
import pandas as pd
import matplotlib.pyplot as plt
import config

def fun_total_goals(data: pd.DataFrame) -> tuple[int, int, int]:
    """
    Calcula los goles totales marcados por locales, visitantes y el global.
    """
    home_goals = int(data['FTHG'].sum())
    away_goals = int(data['FTAG'].sum())
    total_goals = home_goals + away_goals
    
    return home_goals, away_goals, total_goals

def fun_total_goals_by_team(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Calcula los goles marcados por cada equipo como local, visitante y en total.
    """
    # Agrupo y sumamos
    home = data.groupby('HomeTeam')['FTHG'].sum()
    away = data.groupby('AwayTeam')['FTAG'].sum()
    total = home.add(away, fill_value=0).astype(int)
    
    df_home = pd.DataFrame({'Team': home.index, 'Home_Goals': home.values})
    df_away = pd.DataFrame({'Team': away.index, 'Away_Goals': away.values})
    
    df_total = pd.DataFrame({'Team': total.index, 'Total_Goals': total.values})
    df_total = df_total.sort_values(by='Total_Goals', ascending=False)
    
    return df_home, df_away, df_total

def fun_summary_1996_2025(total_points: pd.DataFrame, 
                          home_goals: pd.DataFrame, 
                          away_goals: pd.DataFrame, 
                          total_goals: pd.DataFrame) -> pd.DataFrame:
    """
    Crea un DataFrame resumen uniendo la información de puntos y goles por equipo.
    """
    # Se unen secuencialmente usando el nombre del equipo como clave ('Team')
    summary = total_points.merge(home_goals, on='Team', how='outer')
    summary = summary.merge(away_goals, on='Team', how='outer')
    summary = summary.merge(total_goals, on='Team', how='outer')
    
    # Ordeno por los puntos totales de forma descendente para tener la clasificación real
    summary = summary.sort_values(by='Points', ascending=False).reset_index(drop=True)
    
    return summary

def podium(summary_1996_2025: pd.DataFrame) -> None:
    """
    Genera un diagrama de barras para los 3 mejores equipos.
    """
    # Saco los 3 primeros equipos (asumiendo que el DataFrame ya viene ordenado por puntos)
    top3 = summary_1996_2025.head(3)
    
    # Reordeno manualmente para el efecto pódium: [Segundo, Primero, Tercero]
    equipos = [top3.iloc[1]['Team'], top3.iloc[0]['Team'], top3.iloc[2]['Team']]
    puntos = [top3.iloc[1]['Points'], top3.iloc[0]['Points'], top3.iloc[2]['Points']]
    
    # Colores representativos: Plata, Oro, Bronce
    colores = ['silver', 'gold', '#cd7f32']
    
    plt.figure(figsize=(8, 6))
    
    # Dibujo las barras
    barras = plt.bar(range(3), puntos, color=colores, width=0.6)
    
    # Quito las etiquetas de los ejes 
    plt.xticks([])
    plt.yticks([])
    # Oculto los bordes del gráfico para que quede más limpio
    plt.box(False)
    
    # Añado el nombre del equipo justo encima de cada barra
    for i, barra in enumerate(barras):
        altura = barra.get_height()
        # Coloco el texto un poquito por encima de la barra
        plt.text(barra.get_x() + barra.get_width() / 2, altura + 20, 
                 equipos[i], ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        # Opcional, poner también los puntos dentro de la barra
        plt.text(barra.get_x() + barra.get_width() / 2, altura / 2, 
                 f"{puntos[i]} pts", ha='center', va='center', fontsize=10)

    # Guardado de la imagen
    os.makedirs("src/img", exist_ok=True)
    filename = f"src/img/grafica_ex6_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(filename)
    plt.close()