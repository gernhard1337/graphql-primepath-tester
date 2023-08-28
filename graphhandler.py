from itertools import permutations
import networkx as nx
import copy

baseDatatypes = ["Boolean", "String", "ID", "Int", "Date", "Float", "INPUT_OBJECT"]
nonSchemaTypePrefix = "__"


def buildGraph(graph, type_name, type_dict):
    if type_name.startswith(nonSchemaTypePrefix) or type_name in baseDatatypes:
        pass
    else:
        if type_dict[type_name]['fields']:
            for adjacentNode in type_dict[type_name]['fields']:
                # Überprüfen, ob der Feldtyp LIST oder NON_NULL ist und behandeln entsprechend
                nodeType = adjacentNode['type']
                while nodeType['kind'] in ['LIST', 'NON_NULL']:
                    nodeType = nodeType['ofType']
                if nodeType is None or nodeType['name'] in baseDatatypes:
                    continue

                adjacentNodeName = nodeType['name']
                if not graph.has_edge(type_name, adjacentNodeName):
                    graph.add_edge(type_name, adjacentNodeName)
                    graph[type_name][adjacentNodeName]["data"] = adjacentNode
                    buildGraph(graph, adjacentNodeName, type_dict)


def is_subpath(path, other_path):
    if len(path) > len(other_path):
        return False
    for i in range(len(other_path) - len(path) + 1):
        if path == other_path[i:i+len(path)]:
            return True
    return False


def isPrimePath(path, all_paths):
    for another_path in all_paths:
        if path != another_path and is_subpath(path, another_path):
            return False
    return True


def findPrimePaths_withFilter(startnode, graph):
    all_paths = []
    for end in graph:
        if end != startnode:
            all_paths.extend(findAllPaths(graph, startnode, end))
    prime_paths = [path for path in all_paths if isPrimePath(path, all_paths)]
    return prime_paths


def findNodeCoveragePaths(startnode, graph):
    visited = {node: False for node in graph.nodes()}
    paths = []

    def dfs_path(node, visited, path):
        visited[node] = True
        path.append(node)

        if set(path) == set(graph.nodes()):  # Wenn alle Knoten abgedeckt sind
            paths.append(list(path))

        for neighbour in graph.neighbors(node):
            if visited[neighbour] is False:
                dfs_path(neighbour, visited, path)

        visited[node] = False
        path.pop()

    dfs_path(startnode, visited, [])

    return paths


def findEdgeCoveragePaths(startnode, graph):
    visited = {edge: False for edge in graph.edges()}
    paths = []

    def dfs_path(node, visited, path):
        for neighbour in graph.neighbors(node):
            edge = (node, neighbour)
            if visited[edge] is False:
                visited[edge] = True
                path.append(edge)

                if set(path) == set(graph.edges()):
                    paths.append(list(path))

                dfs_path(neighbour, visited, path)
                visited[edge] = False
                path.pop()

    dfs_path(startnode, visited, [])

    return paths


def findCompletePathCoverage(startnode, graph):
    visited = {node: False for node in graph.nodes()}
    paths = []

    def dfs_path(node, visited, path):
        visited[node] = True
        path.append(node)
        paths.append(list(path))

        for neighbour in graph.neighbors(node):
            if visited[neighbour] is False:
                dfs_path(neighbour, visited, path)

        visited[node] = False
        path.pop()

    dfs_path(startnode, visited, [])

    return paths


def findAllPaths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = findAllPaths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def generate_prime_paths_3(startknoten, g):
    pfadliste = []
    generate_paths(startknoten, [], pfadliste, g)
    return pfadliste


def generate_paths(n, path, pathList, g):
    path.append(n)
    for m in g.successors(n):  # successors gibt die Nachfolger eines Knotens in einem DiGraph wieder
        if m not in path:
            generate_paths(m, copy.deepcopy(path), pathList, g)
    if is_prime_path(path, pathList):
        pathList.append(path)


def is_prime_path(new_path, pathList):
    for exisiting_paths in pathList:
        if is_subpath(new_path, exisiting_paths):
            return False
    return True


def process_lists(lists):
    result = []
    for lst in lists:
        # Doppelte Elemente entfernen, dabei die Reihenfolge beibehalten
        cleaned_list = []
        for item in lst:
            if item not in cleaned_list:
                cleaned_list.append(item)
        # Liste auf maximal Länge 15 kürzen
        result.append(cleaned_list[:15])
    return result


def generate_prime_paths_2(startknoten, g):
    return shortest_path_to_prime(g, startknoten, get_prime_paths(g, startknoten))


def get_prime_paths(G, start_node):
    all_prime_paths = []
    nodes = list(G.nodes())

    for end_node in nodes:
        if end_node == start_node:
            continue
        simple_paths = list(nx.all_simple_paths(G, source=start_node, target=end_node))

        # Ein Pfad ist prime, wenn er nicht als Untermenge eines anderen Pfads betrachtet wird
        prime_paths_for_end_node = []
        for path in simple_paths:
            is_prime = True
            for other_path in simple_paths:
                if set(path).issubset(set(other_path)) and path != other_path:
                    is_prime = False
                    break
            if is_prime:
                prime_paths_for_end_node.append(path)

        all_prime_paths.extend(prime_paths_for_end_node)
    return all_prime_paths


def shortest_path_to_prime(G, start_node, prime_paths):
    shortest_paths = []
    for path in prime_paths:
        try:
            shortest_path = nx.shortest_path(G, source=start_node, target=path[0])
            updated_path = shortest_path + list(path[1:])
            shortest_paths.append(updated_path)
        except nx.NetworkXNoPath:
            pass
    return shortest_paths


def reachHead(path, graph):
    former_nodes = [n for n in graph.nodes() if path[0] in graph[n]]
    for n in former_nodes:
        if n not in path or n == path[-1]:
            return False
    return True


def checkIsPrimePath(path, graph):
    if len(path) >= 2 and path[0] == path[-1]:
        return True
    elif reachHead(path, graph) and reachEnd(path, graph):
        return True
    else:
        return False


def reachEnd(path, graph):
    later_nodes = graph[path[-1]]
    for n in later_nodes:
        if n not in path or n == path[0]:
            return False
    return True


def extendable(path, graph):
    if checkIsPrimePath(path, graph) or reachEnd(path, graph):
        return False
    else:
        return True


def findSimplePath(graph, exPaths, paths=[]):
    paths.extend(filter(lambda p: checkIsPrimePath(p, graph), exPaths))
    exPaths = filter(lambda p: extendable(p, graph), exPaths)
    newExPaths = []
    for p in exPaths:
        for nx in graph[p[-1]]:
            if nx not in p or nx == p[0]:
                newExPaths.append(p + (nx, ))
    if len(newExPaths) > 0:
        findSimplePath(graph, newExPaths, paths)

# Umsetzung von
# https://github.com/heshenghuan/Prime-Path-Coverage/blob/master/PrimePath.py
# in NetworkX mit Anpassungen für GraphQL
def generate_prime_paths(startknoten, g):
    startPaths = [(n, ) for n in g.nodes()]
    simplePaths = []
    findSimplePath(g, startPaths, simplePaths)
    primePaths = sorted(simplePaths, key=lambda a: (len(a), a))
    primePathsWithQueryRoot = shortest_path_to_prime(g, startknoten, primePaths)
    return primePathsWithQueryRoot
















