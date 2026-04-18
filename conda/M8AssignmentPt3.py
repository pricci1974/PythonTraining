import pandas as pd
import networkx as nx

# 1. Load the dataset (CSV with source and target columns)
# Example CSV structure: Source,Target
df = pd.read_csv('socialdata.csv')

# 2. Create the graph
G = nx.from_pandas_edgelist(df, source='football', target='basketball')

# 3. Calculate Centrality Metrics
# Degree Centrality
degree_centrality = nx.degree_centrality(G)
# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)

# 4. Map back to nodes and display
for node in G.nodes():
    print(f"Node {node}: Degree={degree_centrality[node]:.2f}, "
          f"Betweenness={betweenness_centrality[node]:.2f}")