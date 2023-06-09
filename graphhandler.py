import networkx as nx

baseDatatypes = ["Boolean", "String", "ID", "Int", "Date", "Float", "INPUT_OBJECT"]
nonSchemaTypePrefix = "__"


def buildGraph(graph, type_name, type_dict):
    if type_name.startswith(nonSchemaTypePrefix) or type_name in baseDatatypes:
        return
    else:
        for adjacentNode in type_dict[type_name]['fields']:
            if graph.has_edge(adjacentNode['type']['name'], type_name):
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


def findPrimePaths(startnode, graph):
    all_paths = []
    for end in graph:
        if end != startnode:
            all_paths.extend(findAllPaths(graph, startnode, end))
    prime_paths = [path for path in all_paths if isPrimePath(path, all_paths)]
    return prime_paths


def findNodeCoveragePaths(graph):
    return []


def findEdgeCoveragePaths(graph):
    return []


def findFullCoverage(graph):
    return []


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
