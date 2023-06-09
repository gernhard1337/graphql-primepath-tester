from faker import Faker
import random

gen = Faker()


def resolveArg(type, typedict):
    print(type)
    if type["name"] == "ID":
        return "\"" + generateID() + "\""
    if type["name"] == "String":
        return generateString()
    if type["name"] == "Float":
        return str(generateFloat())
    if type["name"] == "Int":
        return str(generateInt())
    if type["name"] == "Boolean":
        return generateBool()
    if type['kind'] == "INPUT_OBJECT":
        return "\"" + generateID() + "\""
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "ID":
        return "[" + "\"" + generateID() + "\"," +  "\"" + generateID() + "\"," + "\"" + generateID() + "\"," + "\"" + generateID() + "\"" + "]"
    return generateString()


def addScalarTypes(type, typedict):
    if type["name"] is None:
        fields = typedict[type["ofType"]["name"]]["fields"]
    else:
        fields = typedict[type["name"]]["fields"]
    fieldString = ""
    for field in fields:
        if field["type"]["kind"] == "SCALAR":
            fieldString = fieldString + " " + field["name"]
    return fieldString


def resolvePathTillOnlyScalarTypesOrEnd(path, typedict, graph, query=""):

    if path:
        edge = path.pop(0)
    else:
        return query

    edge_data = graph[edge[0]][edge[1]]["data"]
    if len(edge_data['args']) < 1:
        query = query + " " + edge_data["name"] + " { " + addScalarTypes(edge_data["type"], typedict) + resolvePathTillOnlyScalarTypesOrEnd(path, typedict, graph, query) + " } "
    else:
        argString = edge_data['name'] + "("
        for args in edge_data['args']:
            argString = argString + args["name"] + ": " + resolveArg(args["type"], typedict)
            if args == edge_data['args'][:-1]:
                argString = argString + ","
        argString = argString + ")"
        query = query + argString + " { " + addScalarTypes(edge_data["type"], typedict) + " " + resolvePathTillOnlyScalarTypesOrEnd(path, typedict, graph, query) + " } "
    return query


def pathToQuery(path, typedict, graph):
    path_edges = list(zip(path[:-1], path[1:]))
    query = "{ " + resolvePathTillOnlyScalarTypesOrEnd(path_edges, typedict, graph) + " }"
    return query


def generateID():
    return gen.uuid4()


def generateString():
    return gen.pystr()


def generateInt():
    return gen.pyint()


def generateBool():
    return gen.pybool()


def generateFloat():
    return gen.pyfloat()





