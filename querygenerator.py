from faker import Faker
import random

gen = Faker()

def resolveArg(type, typedict):
    if type["name"] == "VisibilityScopesEnum":
        return generateGitlabPrivacyEnum()
    if type["name"] == "TypeEnum":
        return generateGitlabTypeEnum()
    if type["name"] == "IssueSort":
        return generateGitlabIssueSortEnum()
    if type["name"] == "IssuableState":
        return generateGitlabIssuableStateEnum()
    if type["name"] == "ID":
        return "\"" + generateID() + "\""
    if type["name"] == "String":
        return "\"" + generateString() + "\""
    if type["name"] == "Float":
        return str(generateFloat())
    if type["name"] == "Int":
        return str(generateInt())
    if type["name"] == "Boolean":
        return str(generateBool()).lower()
    if type["name"] == "Time":
        return  "\"" + str(generateTime()) + "\""
    if type['kind'] == "INPUT_OBJECT" and type["name"] in typedict:
        return generateCustomArg(type["name"], typedict)
    if type["kind"] == "LIST" and type["ofType"]["kind"] == "NON_NULL" and type["ofType"]["ofType"]["name"] == "ID":
        return "[" + "\"" + generateID() + "\"," + "\"" + generateID() + "\"," + "\"" + generateID() + "\"," + "\"" + generateID() + "\"" + "]"
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
        if type["ofType"]["kind"] == "OBJECT":
            fields = typedict[type["ofType"]["name"]]["fields"]
        elif type["ofType"]["ofType"]["kind"] == "OBJECT":
            fields = typedict[type["ofType"]["ofType"]["name"]]["fields"]
    else:
        fields = typedict[type["name"]]["fields"]
    fieldString = ""
    if fields:
        for field in fields:
            if field["type"]["kind"] == "SCALAR":
                fieldString = fieldString + " " + field["name"] + " "
            if field["type"]["kind"] == "NON_NULL" and field["type"]["ofType"]["kind"] == "SCALAR":
                fieldString = fieldString + " " + field["name"] + " "
    return fieldString


def generateTime():
    random_date = gen.date_time_between(start_date='-1y', end_date='now')
    iso_date = random_date.isoformat(timespec='seconds')
    return iso_date


def resolvePathTillOnlyScalarTypesOrEnd(path, typedict, graph, query=""):
    if path:
        edge = path.pop(0)
    else:
        return query
    edge_data = graph[edge[0]][edge[1]]["data"]
    if len(edge_data['args']) < 1:
        if edge_data["type"]["kind"] == "SCALAR":
            query = query + " " + edge_data["name"] + " "
        else:
            query = query + " " + edge_data["name"] + " { " + addScalarTypes(edge_data["type"], typedict) + " " + resolvePathTillOnlyScalarTypesOrEnd(path, typedict, graph, query) + " } "
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


def generateGitlabIssueSortEnum():
    x = random.randint(1, 7)
    if x == 1:
        return "updated_desc"
    if x == 2:
        return "updated_asc"
    if x == 3:
        return "created_desc"
    if x == 4:
        return "created_asc"
    if x == 5:
        return "DUE_DATE_ASC"
    if x == 6:
        return "DUE_DATE_DESC"
    if x == 7:
        return "RELATIVE_POSITION_ASC"


def generateGitlabIssuableStateEnum():
    x = random.randint(1, 3)
    if x == 1:
        return "opened"
    if x == 2:
        return "closed"
    if x == 3:
        return "locked"


def generateGitlabTypeEnum():
    x = random.randint(1, 2)
    if x == 1:
        return "personal"
    if x == 2:
        return "project"


def generateGitlabPrivacyEnum():
    x = random.randint(1, 3)
    if x == 1:
        return "private"
    if x == 2:
        return "internal"
    if x == 3:
        return "public"


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