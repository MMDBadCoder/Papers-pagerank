from graph.graph_builder import get_graph_of_authors

top_papers_count = 50
walk_len = 100
walk_count = 100
alpha = 0.95
printing_top_authors_count = 10

links = get_graph_of_authors(top_papers_count)

# **********************  Using ready library  ************************
# import networkx as nx
# D = nx.DiGraph()
# D.add_weighted_edges_from(graph)
# result = nx.pagerank(D, alpha=0.99999, max_iter=10)

# **********************  Using my own process  ************************
from my_pagerank.pagerank import edge_weighted_pagerank
result = edge_weighted_pagerank(links, alpha, walk_count, walk_len)

# printing top authors
print(len(result))
for top_item in sorted(result.items(), key=lambda item: 1 - item[1])[:printing_top_authors_count]:
    print(top_item)
