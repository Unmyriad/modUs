"""
Max-Cut Graph Generator.

This script generates random graphs using NetworkX library for the Max-Cut problem. The generated graph is used for executing quantum optimization algorithm via Qiskit.
"""

def generate_graph(nodes, probability):
    """Generate a graph with custom nodes and probability using NetworkX.
    
    Args:
        nodes (int): the number of nodes to be generated
        probability (float): the likelihood that a connection occurs between a pair of nodes
    
    Return:
        graph (graph): A graph that has custom amount of nodes
    """
    import networkx as nx
    import matplotlib.pyplot as plt
    
    graph = nx.erdos_renyi_graph(nodes, probability, seed=42)
    
    nx.draw(graph, with_labels=True)
    plt.show()
    print(type(graph))
    
    return graph
    


generate_graph(50, 0.3)
    
    
