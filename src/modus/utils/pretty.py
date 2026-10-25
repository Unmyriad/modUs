import json

def pretty_print(graph, indent=2):
    """Provides a readable JSON output

    Args:
        graph (dict): Max-Cut problem to be printed
        indent (int, optional): How much should be indented Defaults to 2.

    Returns:
        pretty_graph: returns a readable JSON output
    """
    pretty_graph = json.dumps(graph, indent=indent)
    return pretty_graph