from faker import Faker
import random

gen = Faker()


def resolveArg(type, typedict):
    if type["name"] == "ID":
        return "\"" + generateID() + "\""
    if type["name"] == "String":
        return "\"" + generateString() + "\""
    if type["name"] == "Float":
        return str(generateFloat())
    if type["name"] == "Int":
        return str(generateInt())
    if type["name"] == "Boolean":
        return str(generateBool())
    if type['kind'] == "INPUT_OBJECT" and type["name"] in typedict:
        return generateCustomArg(type["name"], typedict)
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "ID":
        return "[" + "\"" + generateID() + "\"," + "\"" + generateID() + "\"," + "\"" + generateID() + "\"," + "\"" + generateID() + "\"" + "]"
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "String":
        return "[" + "\"" + generateString() + "\"," + "\"" + generateString() + "\"," + "\"" + generateString() + "\"," + "\"" + generateString() + "\"" + "]"
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "Float":
        return "[" + "\"" + generateFloat() + "\"," + "\"" + generateFloat() + "\"," + "\"" + generateFloat() + "\"," + "\"" + generateFloat() + "\"" + "]"
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "Int":
        return "[" + "\"" + generateInt() + "\"," + "\"" + generateInt() + "\"," + "\"" + generateInt() + "\"," + "\"" + generateInt() + "\"" + "]"
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "Boolean":
        return "[" + "\"" + generateBool() + "\"," + "\"" + generateBool() + "\"," + "\"" + generateBool() + "\"," + "\"" + generateBool() + "\"" + "]"
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["kind"] == 'ID':
        return "\"" + generateID() + "\""
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["kind"] == 'String':
        return "\"" + generateString() + "\""
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["kind"] == 'Float':
        return str(generateFloat())
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["kind"] == 'Int':
        return str(generateInt())
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["kind"] == 'Boolean':
        return str(generateBool())
    return "\"" + generateString() + "\""


def addScalarTypes(type, typedict):
    if type["name"] is None:
        fields = typedict[type["ofType"]["name"]]["fields"]
    else:
        fields = typedict[type["name"]]["fields"]
    fieldString = ""
    for field in fields:
        if field["type"]["kind"] == "SCALAR":
            fieldString = fieldString + " " + field["name"]
        if field["type"]["kind"] == "NON_NULL" and field["type"]["ofType"]["kind"] == "SCALAR":
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
    elif len(edge_data['args']) < 1 and (edge_data["type"]["kind"] == "OBJECT" or edge_data["type"]["kind"] == "LIST"):
        query = query + " { " + addScalarTypes(edge_data["type"],  typedict) + " " + resolvePathTillOnlyScalarTypesOrEnd(path, typedict, graph, query) + " } "
    else:
        argString = edge_data['name'] + "("
        for args in edge_data['args']:
            argString = argString + args["name"] + ": " + resolveArg(args["type"], typedict) + ", "
        argString = argString + ")"
        query = query + argString + " { " + addScalarTypes(edge_data["type"], typedict) + " " + resolvePathTillOnlyScalarTypesOrEnd(path, typedict, graph, query) + " } "
    return query


def pathToQuery(path, typedict, graph):
    path_edges = list(zip(path[:-1], path[1:]))
    query = "{ " + resolvePathTillOnlyScalarTypesOrEnd(path_edges, typedict, graph) + " }"
    return query


def generateID():
    x = random.randint(1, 2)
    if x == 1:
        return str(gen.pyint())
    else:
        return gen.uuid4()


def generateString():
    return gen.pystr()


def generateInt():
    return gen.pyint()


def generateBool():
    return gen.pybool()


def generateFloat():
    return gen.pyfloat()


def generateCustomArg(type, typedict):
    argspec = typedict[type]["inputFields"]
    customArgString = "{"
    for fields in argspec:
        if fields["type"]["name"] == "String":
            customArgString = customArgString + fields["name"] + ": " + "\"" + generateString() + "\"" + ","
        if fields["type"]["name"] == "Int":
            customArgString = customArgString + fields["name"] + ": " + generateInt() + ","
        if fields["type"]["name"] == "Boolean":
            customArgString = customArgString + fields["name"] + ": " + generateBool() + ","
        if fields["type"]["name"] == "Float":
            customArgString = customArgString + fields["name"] + ": " + generateFloat() + ","
        if fields["type"]["name"] == "ID":
            customArgString = customArgString + fields["name"] + ": " + generateID() + ","
    customArgString = customArgString + "}"
    return customArgString