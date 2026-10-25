import networkx as nx
import logging
from typing import Dict

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_max_cut(problem_size: int, edge_probability: float, seed: int = 42) -> Dict:
    """Generate Max-Cut Problem

    Args:
        problem_size (int): the number of nodes in graph
        edge_probability (float): The likelihood of of two nodes connecting
        seed (int, optional): Random seed . Defaults to 42.

    Returns:
        problem (dict): Dictionary containing the graph and node size
    """
    