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


def addScalarTypes(type, typedict, name):
    if type["name"] is None:
        if type["kind"] in ["NON_NULL", "LIST"] and type["ofType"]["kind"] == "SCALAR":
            return name
        if type["ofType"]["kind"] == "ENUM":
            return name
        if type["ofType"]["kind"] == "OBJECT":
            fields = typedict[type["ofType"]["name"]]["fields"]
        elif type["ofType"]["ofType"]["kind"] == "OBJECT":
            fields = typedict[type["ofType"]["ofType"]["name"]]["fields"]
        elif type["ofType"]["ofType"]["ofType"]["kind"] == "OBJECT":
            fields = typedict[type["ofType"]["ofType"]["ofType"]["name"]]["fields"]
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
            query = query + " " + edge_data["name"] + " { " + addScalarTypes(edge_data["type"], typedict, edge_data["name"]) + " " + resolvePathTillOnlyScalarTypesOrEnd(path, typedict, graph, query) + " } "
    else:
        argString = edge_data['name'] + "("
        for args in edge_data['args']:
            argString = argString + args["name"] + ": " + resolveArg_ToyAdjustments(args["type"], typedict) + ", "
        argString = argString + ")"
        query = query + argString + " { " + addScalarTypes(edge_data["type"], typedict, edge_data["name"]) + " " + resolvePathTillOnlyScalarTypesOrEnd(path, typedict, graph, query) + " } "
    return query


def pathToQuery(path, typedict, graph):
    path_edges = list(zip(path[:-1], path[1:]))
    # change resolvePathTillOnlyScalarTypesOrEnd_GitLab to resolvePathTillOnlyScalarTypesOrEnd if not running gitlab
    query = "{ " + resolvePathTillOnlyScalarTypesOrEnd(path_edges, typedict, graph) + " }"
    return query


def generateID():
    return 1
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


########################
# mocked Argumentgenerators for Toy-Experiment
########################


def resolveArg_ToyAdjustments(type, typedict):
    if type["name"] == "VisibilityScopesEnum":
        return generateGitlabPrivacyEnum()
    if type["name"] == "TypeEnum":
        return generateGitlabTypeEnum()
    if type["name"] == "PipelineStatusEnum":
        return generateGitlabPipelineStatusEnum()
    if type["name"] == "VisibilityLevelsEnum":
        return generateGitlabVisibilityLevelsEnum()
    if type["name"] == "TodoActionEnum":
        return generateGitlabTodoActionEnum()
    if type["name"] == "TodoStateEnum":
        return generateGitlabTodoStateEnum()
    if type["name"] == "TodoTargetEnum":
        return generateGitlabTodoTargetEnum()
    if type["name"] == "IssueSort":
        return generateGitlabIssueSortEnum()
    if type["name"] == "IssuableState":
        return generateGitlabIssuableStateEnum()
    if type["name"] == "ID":
        return "\"" + generateIDToy() + "\""
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
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["name"] == 'ID':
        return "\"" + generateIDToy() + "\""
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["name"] == 'String':
        return "\"" + generateString() + "\""
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["name"] == 'Float':
        return str(generateFloat())
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["name"] == 'Int':
        return str(generateInt())
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["name"] == 'Boolean':
        return str(generateBool())
    return "\"" + generateString() + "\""


def generateIDToy():
    x = random.randint(0, 4)
    possibleIds = [1, 2, 100, 200, "TEST"]
    return str(possibleIds[x])


########################
# mocked Argumentgenerators for GitLab-Experiment
# GitLab has some hard limitations that we need to handle so this
# mocks are harder than before
########################


def resolvePathTillOnlyScalarTypesOrEnd_GitLab(path, typedict, graph, query=""):
    if path:
        edge = path.pop(0)
    else:
        return query
    edge_data = graph[edge[0]][edge[1]]["data"]
    if len(edge_data['args']) < 1:
        if edge_data["type"]["kind"] == "SCALAR" or (edge_data["type"]["kind"] == "NON_NULL" and edge_data["type"]["ofType"]["kind"] == "SCALAR")or (edge_data["type"]["kind"] == "NON_NULL" and edge_data["type"]["ofType"]["kind"] == "ENUM"):
            query = query + " " + edge_data["name"] + " "
        else:
            query = query + " " + edge_data["name"] + " { " + addScalarTypes(edge_data["type"], typedict, edge_data["name"]) + " " + resolvePathTillOnlyScalarTypesOrEnd_GitLab(path, typedict, graph, query) + " } "
    else:
        if not path:
            return query
        argString = edge_data['name'] + "("
        for args in edge_data['args']:
            if not any(sub in argString for sub in ["authorId:", "projectId:", "author:", "project:"]):
                argString = argString + args["name"] + ": " + resolveArg_GitLab(args["type"], typedict, args["name"]) + ", "
        argString = argString + ")"
        query = query + argString + " { " + addScalarTypes(edge_data["type"], typedict, edge_data["name"]) + " " + resolvePathTillOnlyScalarTypesOrEnd_GitLab(path, typedict, graph, query) + " } "
    return query


def resolveArg_GitLab(type, typedict, typename):
    if typename == "fullPath":
        return "\"" + generateGitLabFullPathUrl() + "\""
    if type["name"] == "VisibilityScopesEnum":
        return generateGitlabPrivacyEnum()
    if type["name"] == "TypeEnum":
        return generateGitlabTypeEnum()
    if type["name"] == "PipelineStatusEnum":
        return generateGitlabPipelineStatusEnum()
    if type["name"] == "VisibilityLevelsEnum":
        return generateGitlabVisibilityLevelsEnum()
    if type["name"] == "TodoActionEnum":
        return generateGitlabTodoActionEnum()
    if type["name"] == "TodoStateEnum":
        return generateGitlabTodoStateEnum()
    if type["name"] == "TodoTargetEnum":
        return generateGitlabTodoTargetEnum()
    if type["name"] == "IssueSort":
        return generateGitlabIssueSortEnum()
    if type["name"] == "IssuableState":
        return generateGitlabIssuableStateEnum()
    if type["name"] == "ID":
        return "\"" + generateIDGitLab() + "\""
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
        return "[" + "\"" + generateIDGitLab() + "\"," + "\"" + generateIDGitLab() + "\"," + "\"" + generateIDGitLab() + "\"," + "\"" + generateIDGitLab() + "\"" + "]"
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "ID":
        return "[" + "\"" + generateIDGitLab() + "\"," + "\"" + generateIDGitLab() + "\"," + "\"" + generateIDGitLab() + "\"," + "\"" + generateIDGitLab() + "\"" + "]"
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "String":
        return "[" + "\"" + generateString() + "\"," + "\"" + generateString() + "\"," + "\"" + generateString() + "\"," + "\"" + generateString() + "\"" + "]"
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "Float":
        return "[" + "\"" + generateFloat() + "\"," + "\"" + generateFloat() + "\"," + "\"" + generateFloat() + "\"," + "\"" + generateFloat() + "\"" + "]"
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "Int":
        return "[" + "\"" + generateInt() + "\"," + "\"" + generateInt() + "\"," + "\"" + generateInt() + "\"," + "\"" + generateInt() + "\"" + "]"
    if type["ofType"]["kind"] == "LIST" and type["ofType"]["ofType"]["ofType"]["name"] == "Boolean":
        return "[" + "\"" + generateBool() + "\"," + "\"" + generateBool() + "\"," + "\"" + generateBool() + "\"," + "\"" + generateBool() + "\"" + "]"
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["name"] == 'ID':
        return "\"" + generateIDGitLab() + "\""
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["name"] == 'String':
        return "\"" + generateString() + "\""
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["name"] == 'Float':
        return str(generateFloat())
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["name"] == 'Int':
        return str(generateInt())
    if type["kind"] == "NON_NULL" and type["ofType"]["kind"] == 'SCALAR' and type["ofType"]["name"] == 'Boolean':
        return str(generateBool())
    if type["kind"] == "LIST" and type["ofType"]["kind"] == 'NON_NULL' and type["ofType"]["ofType"]["name"] == "TodoActionEnum":
        values = set()
        while len(values) < 4:
            values.add(generateGitlabTodoActionEnum())
        values = list(values)
        result_string = "[" + ",".join(f'"{value}"' for value in values) + "]"
        return result_string
    return "\"" + generateString() + "\""


def generateGitLabFullPathUrl():
    choices = [r'e\u0000', "groupx_0/projectx_0_2", "",  "groupx_0", "1", "groupx_3/projectx_2_1"]
    x = random.randint(0, len(choices)-1)
    return choices[x]


def generateIDGitLab():
    snippedId1 = random.randint(0,50)
    snippedId2 = random.randint(0, 50)
    snippedId3 = random.randint(0, 50)
    possibleIds = ["groupx_0", r'e\u0000', "gid://gitlab/PersonalSnippet/"+str(snippedId1), "gid://gitlab/PersonalSnippet/"+str(snippedId2), "gid://gitlab/PersonalSnippet/"+str(snippedId3)]
    x = random.randint(0, len(possibleIds)-1)
    return str(possibleIds[x])


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


def generateGitlabPipelineStatusEnum():
    enumVals = ["CREATED", "PREPARING", "PENDING", "RUNNING", "FAILED", "SUCCESS", "CANCELED", "SKIPPED", "MANUAL", "SCHEDULED"]
    x = random.randint(0, 9)
    return enumVals[x]


def generateGitlabVisibilityLevelsEnum():
    enumVals = ["PRIVATE", "INTERNAL", "PUBLIC"]
    x = random.randint(0, 2)
    return enumVals[x]


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


def generateGitlabTodoTargetEnum():
    enumVals = ["COMMIT", "ISSUE", "MERGEREQUEST"]
    x = random.randint(0, 2)
    return enumVals[x]


def generateGitlabTodoActionEnum():
    enumVals = ["ASSIGNED", "MENTIONED", "BUILD_FAILED", "MARKED", "APPROVAL_REQUIRED", "UNMERGEABLE"]
    x = random.randint(0, 5)
    return enumVals[x]


def generateGitlabTodoStateEnum():
    enumVals = ["PENDING", "DONE"]
    x = random.randint(0, 1)
    return enumVals[x]