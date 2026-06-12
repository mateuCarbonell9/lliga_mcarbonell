import os
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import config

def graf(data: pd.DataFrame, selected_teams: list[str]) -> None:
    """
    Genera un grafo de conexiones entre los 5 mejores equipos históricos.
    Muestra una única línea por enfrentamiento con el total de partidos jugados.
    """
    # 1. Filtramos el dataset para quedarnos solo con partidos entre estos 5 equipos
    filtro = (data['HomeTeam'].isin(selected_teams)) & (data['AwayTeam'].isin(selected_teams))
    df_filtered = data[filtro]

    # 2. Creamos un grafo no dirigido
    G = nx.Graph()
    G.add_nodes_from(selected_teams)

    # 3. Truco para agrupar idas y vueltas: 
    # Ordenamos los dos equipos alfabéticamente para que A vs B sea igual a B vs A
    pares = df_filtered.apply(lambda row: tuple(sorted([row['HomeTeam'], row['AwayTeam']])), axis=1)
    
    # Contamos cuántas veces se repite cada enfrentamiento
    conteos = pares.value_counts().to_dict()

    # 4. Añadimos las líneas (aristas) con su peso (número de partidos)
    for (equipo1, equipo2), partidos in conteos.items():
        G.add_edge(equipo1, equipo2, weight=partidos)

    # 5. Dibujamos el grafo
    plt.figure(figsize=(10, 8))
    
    # 'circular_layout' reparte a los 5 equipos formando un pentágono perfecto
    pos = nx.circular_layout(G) 
    
    # Dibujar los equipos (nodos) y las líneas (aristas)
    nx.draw(G, pos, with_labels=True, node_color='lightsteelblue', 
            node_size=3500, font_size=9, font_weight='bold', 
            edge_color='gray', width=2)
    
    # Dibujar los números encima de las líneas (etiquetas)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=11)
    
    plt.title('Enfrentamientos entre el Top 5 Histórico')
    
    # Guardado de la imagen
    os.makedirs("src/img", exist_ok=True)
    filename = f"src/img/grafica_ex7_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(filename)
    plt.close()