import pandas as pd

def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """
    Añade las columnas points_home y points_away en función del resultado.
    """
    df = data.copy()
    
    # Asignamos los puntos (Victoria: 3, Empate: 1, Derrota: 0)
    df['points_home'] = df['FTR'].map({'H': 3, 'D': 1, 'A': 0})
    df['points_away'] = df['FTR'].map({'H': 0, 'D': 1, 'A': 3})
    
    return df

def fun_total_points(data: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    """
    Calcula los puntos totales acumulados desde 1995 por cada equipo.
    Devuelve la información redundante solicitada: (Series, DataFrame).
    """
    # Se suman los puntos conseguidos en casa por cada equipo
    home_points = data.groupby('HomeTeam')['points_home'].sum()
    
    # Sumo los puntos conseguidos fuera
    away_points = data.groupby('AwayTeam')['points_away'].sum()
    
    # Sumo ambos totales
    total_series = home_points.add(away_points, fill_value=0).astype(int)
    total_series = total_series.sort_values(ascending=False)
    total_series.name = 'Points'
    
    # Convertimos la Series a DataFrame
    total_df = total_series.reset_index()
    total_df.columns = ['Team', 'Points']
    
    return total_series, total_df

def alltime_winner(df_total_points: pd.DataFrame) -> str:
    """
    Devuelve el equipo que ha acumulado más puntos.
    """
    # Como el DataFrame ya viene ordenado de mayor a menor, cogemos el primero
    winner = df_total_points.iloc[0]['Team']
    return winner