"""
Punto de entrada principal para la PEC4.
Ejecuta los ejercicios de forma incremental.
"""
import argparse
import sys
from config import nom_alumne, date_time

# Importamos solo las funciones del Ejercicio 1 por ahora
from exercises.ex1 import load_and_eda, plot_home_away_goals
from exercises.ex2 import total_matches, plot_matches_team_total
from exercises.ex3 import goals_distribution, plot_goals_ditribution
from exercises.ex4 import FTR, plot_FTR
from exercises.ex5 import add_points, fun_total_points, alltime_winner
from exercises.ex6 import fun_total_goals, fun_total_goals_by_team, fun_summary_1996_2025, podium
from exercises.ex7 import graf

def main():
    """Función principal que gestiona los argumentos y la ejecución."""
    parser = argparse.ArgumentParser(description="Ejecución de la PEC4 - Liga de Fútbol 1995-2025")
    parser.add_argument('-ex', type=int, choices=range(1, 8), 
                        help="Ejecuta los ejercicios de forma incremental hasta el número indicado (1-7).")
    
    args = parser.parse_args()

    if not args.ex:
        print("Por favor, indica un ejercicio a ejecutar usando el argumento -ex.")
        parser.print_help()
        sys.exit(1)

    print(f"--- Iniciando ejecución para el alumno: {nom_alumne} ---")
    print(f"--- Timestamp: {date_time} ---\n")

    # Ruta relativa al dataset
    csv_path = "src/data/LaLiga_Matches.csv" # Asegúrate de que el nombre coincida

    # La lógica incremental
    if args.ex >= 1:
        print("=== EJERCICIO 1 ===")
        print("Cargando dataset y realizando EDA...")
        
        # Ejecutamos la función de carga
        df_liga = load_and_eda(csv_path)
        
        # Hacemos los prints EXCLUSIVAMENTE aquí en main.py
        print("\n--- Primeros 5 registros ---")
        print(df_liga.head())
        print("\n--- Últimos 5 registros ---")
        print(df_liga.tail())
        print("\n--- Información relevante del dataset ---")
        print(df_liga.info())
        
        print("\nGenerando gráfica de distribución de goles (boxplot)...")
        plot_home_away_goals(df_liga)
        print("Ejercicio 1 completado con éxito. Gráfica guardada en img/\n")

    if args.ex >= 2:
        print("=== EJERCICIO 2 ===")
        print("Calculando partidos totales...")
        
        # Como es incremental, aprovechamos el csv_path definido antes
        df_liga = load_and_eda(csv_path)
        
        # Ejecutamos la función
        matches_team_total = total_matches(df_liga)
        
        # 1. Mostrar los 10 primeros valores
        print("\n--- Top 10 equipos con más partidos ---")
        print(matches_team_total.head(10))
        
        # 2. Mostrar los equipos que siempre han estado en primera (máximo de partidos)
        max_partidos = matches_team_total['Total_Matches'].max()
        equipos_max = matches_team_total[matches_team_total['Total_Matches'] == max_partidos]
        
        print(f"\n--- Equipos con el máximo de partidos ({max_partidos}) ---")
        print(equipos_max['Team'].to_string(index=False))
        
        # 3. Generar la gráfica
        print("\nGenerando gráfica de partidos totales...")
        plot_matches_team_total(matches_team_total)
        print("Ejercicio 2 completado. Gráfica guardada en src/img/\n")

    if args.ex >= 3:
        print("=== EJERCICIO 3 ===")
        print("Calculando distribución de goles...")
        
        df_liga = load_and_eda(csv_path)
        distr_goals_home, distr_goals_away = goals_distribution(df_liga)
        
        print("\n--- Distribución de goles en casa ---")
        print(distr_goals_home)
        
        print("\n--- Distribución de goles fuera ---")
        print(distr_goals_away)
        
        print("\nGenerando gráfica de distribución...")
        plot_goals_ditribution(distr_goals_home, distr_goals_away)
        print("Ejercicio 3 completado. Gráfica guardada en src/img/\n")
    
    if args.ex >= 4:
        print("=== EJERCICIO 4 ===")
        print("Analizando victorias y empates...")
        
        df_liga = load_and_eda(csv_path)
        ftr_df = FTR(df_liga)
        
        print("\n--- Resultados Totales ---")
        print(ftr_df)
        
        # Calcular porcentaje de partidos que ganan los locales
        total_partidos = ftr_df['Matches'].sum()
        # Extraemos el número exacto de victorias locales (donde Result es 'H')
        wins_home = ftr_df.loc[ftr_df['Result'] == 'H', 'Matches'].values[0]
        porcentaje_local = (wins_home / total_partidos) * 100
        
        print(f"\n¿Qué porcentaje de partidos ganan los locales?")
        print(f"Respuesta: {porcentaje_local:.2f}%")
        
        print("\nGenerando gráfica de resultados (FTR)...")
        plot_FTR(ftr_df)
        print("Ejercicio 4 completado. Gráfica guardada en src/img/\n")
    
    if args.ex >= 5:
        print("=== EJERCICIO 5 ===")
        print("Calculando la clasificación global histórica...")
        
        df_liga = load_and_eda(csv_path)
        
        # 1. Añadimos los puntos
        df_liga_points = add_points(df_liga)
        print("\n--- Primeros 10 valores con puntos añadidos ---")
        # Mostramos las columnas relevantes para comprobar que ha funcionado
        columnas_ver = ['HomeTeam', 'AwayTeam', 'FTR', 'points_home', 'points_away']
        print(df_liga_points[columnas_ver].head(10))
        
        # 2. Calculamos totales (recibiendo la tupla)
        series_puntos, df_puntos = fun_total_points(df_liga_points)
        print("\n--- Top 10 equipos por puntos totales (DataFrame) ---")
        print(df_puntos.head(10))
        
        # 3. Obtenemos al ganador
        ganador = alltime_winner(df_puntos)
        print(f"\n¡El ganador histórico de la Liga (1995-2020) es: {ganador}!")
        print("Ejercicio 5 completado.\n")
    
    if args.ex >= 6:
        print("=== EJERCICIO 6 ===")
        print("Construyendo el DataFrame Summary y el Podium...")
        
        df_liga = load_and_eda(csv_path)
        
        # 1. Total de goles globales
        home_g, away_g, total_g = fun_total_goals(df_liga)
        print(f"\nGoles totales -> Local: {home_g} | Visitante: {away_g} | Global: {total_g}")
        
        # 2. Goles por equipo
        df_home_goals, df_away_goals, df_total_goals = fun_total_goals_by_team(df_liga)
        print("\n--- Primeros 10 valores de goles totales por equipo ---")
        print(df_total_goals.head(10))
        
        # 3. Necesitamos los puntos del ejercicio 5 para construir el summary
        df_liga_points = add_points(df_liga)
        _, df_total_points = fun_total_points(df_liga_points)
        
        # 4. Construimos el DataFrame de resumen
        summary_df = fun_summary_1996_2025(df_total_points, df_home_goals, df_away_goals, df_total_goals)
        print("\n--- Primeros valores del Summary 1995-2025 ---")
        print(summary_df.head())
        
        # 5. Generamos el podium
        print("\nGenerando el Pódium de los mejores equipos...")
        podium(summary_df)
        print("Ejercicio 6 completado. Gráfica guardada en src/img/\n")

    if args.ex >= 7:
        print("=== EJERCICIO 7 ===")
        print("Generando el grafo de conexiones del Top 5...")
        
        df_liga = load_and_eda(csv_path)
        
        # Reconstruimos la clasificación para sacar a los 5 mejores
        df_liga_points = add_points(df_liga)
        _, df_total_points = fun_total_points(df_liga_points)
        df_home_goals, df_away_goals, df_total_goals = fun_total_goals_by_team(df_liga)
        summary_df = fun_summary_1996_2025(df_total_points, df_home_goals, df_away_goals, df_total_goals)
        
        # Extraemos la lista con los nombres de los 5 mejores equipos
        top5_teams = summary_df['Team'].head(5).tolist()
        print(f"Equipos seleccionados para el grafo: {', '.join(top5_teams)}")
        
        # Ejecutamos la función
        graf(df_liga, top5_teams)
        print("Ejercicio 7 completado. Grafo guardado en src/img/\n")
        print(f"--- Ejecución finalizada con éxito para {nom_alumne} ---")
if __name__ == "__main__":
    main()