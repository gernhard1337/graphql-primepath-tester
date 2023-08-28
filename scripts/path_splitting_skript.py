# Splits generated paths to validate our generated prime paths
# Importieren der benötigten Bibliotheken
def extract_nodes_edges(file_path):
    nodes = set()
    edges = set()

    with open(file_path, 'r') as file:
        for line in file:
            # Entfernen von Leerzeichen und Aufteilen der Zeile in Knoten
            path = line.strip().split(' -> ')

            # Hinzufügen aller Knoten zum Set "nodes"
            nodes.update(path)

            # Erzeugen von Kanten aus aufeinanderfolgenden Knoten und Hinzufügen zum Set "edges"
            for i in range(len(path) - 1):
                edges.add((path[i], path[i+1]))

    return nodes, edges

def print_nodes_edges(nodes, edges):
    print("Nodes:")
    for node in nodes:
        print(node)

    print("\nEdges:")
    for edge in edges:
        print(f'{edge[0]} {edge[1]}')


if __name__ == "__main__":
    nodes, edges = extract_nodes_edges('../experiment/first run/paths.txt')
    print_nodes_edges(nodes, edges)