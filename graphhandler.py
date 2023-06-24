from itertools import permutations

import networkx as nx

baseDatatypes = ["Boolean", "String", "ID", "Int", "Date", "Float", "INPUT_OBJECT"]
nonSchemaTypePrefix = "__"


def buildGraph(graph, type_name, type_dict):
    if type_name.startswith(nonSchemaTypePrefix) or type_name in baseDatatypes:
        pass
    else:
        for adjacentNode in type_dict[type_name]['fields']:
            if graph.has_edge(type_name, adjacentNode['type']['name']):
                return
            else:
                if adjacentNode['type']['name'] and adjacentNode['type']['name'] not in baseDatatypes:

                    graph.add_edge(type_name, adjacentNode['type']['name'])
                    graph[type_name][adjacentNode['type']['name']]["data"] = adjacentNode
                    buildGraph(graph, adjacentNode['type']['name'], type_dict)
                if adjacentNode['type']['kind'] == 'LIST' and adjacentNode['type']['ofType']['name'] not in baseDatatypes:
                    graph.add_edge(type_name, adjacentNode['type']['ofType']['name'])
                    graph[type_name][adjacentNode['type']['ofType']['name']]["data"] = adjacentNode
                    buildGraph(graph, adjacentNode['type']['ofType']['name'], type_dict)


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


def generate_prime_paths(startnode, graph):
    def visit(node, path):
        nonlocal paths
        nonlocal visited
        if node not in path:
            path = path + [node]
            if len(path) > 2 and any(path in p for p in paths if len(path) < len(p)):
                pass
            else:
                paths = [p for p in paths if not (set(path).issubset(set(p)) and len(path) <= len(p))]
                paths.append(path)
                for next_node in graph[node]:
                    visit(next_node, path)

    paths = []
    visited = set()
    visit(startnode, [])
    return paths

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
