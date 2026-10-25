import networkx as nx
import logging
from typing import Dict, Any
from modus.utils.pretty import pretty_print

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_max_cut(problem_size: int = 20, edge_probability: float = 0.5, seed: int = 42) -> Dict:
    """Generate Max-Cut Problem

    Args:
        problem_size (int): the number of nodes in graph
        edge_probability (float): The likelihood of of two nodes connecting
        seed (int, optional): Random seed . Defaults to 42.

    Returns:
        problem (dict): Dictionary containing the graph and node size
    """
    G = nx.erdos_renyi_graph(problem_size, edge_probability, seed)
    
    
    if not nx.is_connected(G):
        logger.warning("Graph has no nodes")
        return generate_max_cut(problem_size, edge_probability, seed)
    
    graph_dict = nx.to_dict_of_dicts(G)
    
    # P4oblem Dictionary
    problem = {
        "problem_size": problem_size,
        "graph": graph_dict
    }
    
    # Add to Logging
    logger.info(f"Generated a problem with {problem_size} nodes and {edge_probability} edge probability")
    problem = pretty_print(problem)
    return problem