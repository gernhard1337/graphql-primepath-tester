# fremde Imports
import matplotlib.pyplot as plt
import networkx as nx
import json
import requests
import sys
import pytest
# eigene Imports
import queries
import graphhandler
import querygenerator
import pytestgenerator

# testUrls die funktionieren sollten
# https://rickandmortyapi.com/graphql -> works
# https://countries.trevorblades.com/graphql -> works but not in fullest
#
# http://localhost:4000/graphql -> run minimaltestServer2.js, all works
# testoken docker windows e9EwB-bNkKDrzECcy-qB

## For Gitlab Test
TOKEN = "3Yzwxep5AQwjXrff7bPE"
GITLAB_URL = "http://localhost"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


if 0 in sys.argv:
    testUrl = sys.argv[0]
else:
    testUrl = "https://rickandmortyapi.com/graphql"

if 1 in sys.argv:
    testPerPath = sys.argv[1]
else:
    testPerPath = 5

# Schema Query
# normal query
# r = requests.post(testUrl, json={'query': queries.introspection_query}, headers={'Authorization': 'access_token e9EwB-bNkKDrzECcy-qB'})
# query in gitlab
print("Introspection Query")
r = requests.post(testUrl, json={'query': queries.introspection_query}, headers=HEADERS)

json_data = json.loads(r.text)
with open('schema.json', 'w') as f:
    json.dump(json_data, f)

# Graph aus Query
graph = nx.DiGraph()
type_dict = {gqltype['name']: gqltype for gqltype in json_data['data']['__schema']['types']}

with open('dict.json', "w") as f:
    json.dump(type_dict, f)

# PrimePaths finden - change method for other coverage if wanted
print("Building Graph")
graphhandler.buildGraph(graph, "Query", type_dict)
print("Generating Path")
paths = graphhandler.generate_prime_paths("Query", graph)
# experimentell mal noch andere Pfade die andere Kriterien umsetzen hinzufügen
#for path in graphhandler.findCompletePathCoverage("Query", graph):
#    primePaths.append(path)
#for path in graphhandler.findNodeCoveragePaths("Query", graph):
#    primePaths.append(path)
#for path in graphhandler.findEdgeCoveragePaths("Query", graph):
#    primePaths.append(path)


# PrimePaths zu Query
print("generating Querys from Path")
f = open("paths.txt", "w")

for primePath in paths:
    f.write(" -> ".join(primePath))
    f.write("\n")
f.close()

######
# gitlab has a depth-limit of 15. To assure this, we need to cut
# the paths to this max length. Experiments showed that from schema paths up to length of 20 were produced
# comment the following line if not running on gitlab test
paths = graphhandler.process_lists(paths)

primePathQueries = []
for primePath in paths:
    # 5 Tests pro Pfad
    for x in range(testPerPath):
        primePathQueries.append(querygenerator.pathToQuery(primePath, type_dict, graph))


##############
# Testsuite using pytest
# saves a file with pytest-tests; these need to get run individually
###########
print("adding tests to Test File")
fileString = ""
f = open("test_GraphQL.py", "w")
f.write("import requests")
f.write("\n")
f.write("import queries")
f.write("\n")
f.write("import json")
f.write("\n")
f.write("import logging")
f.write("\n")
f.write("\n")
for testQuery in primePathQueries:
    f.write(pytestgenerator.generateTestFromQuery(testQuery, testUrl))
f.close()


################
# Self-defined Testsuite
###############
print("Running Querys")

f = open("queries+results.txt", "w")

queryResults = []
for testQuery in primePathQueries:
    r = requests.post(testUrl, json={'query': testQuery}, headers=HEADERS)
    response_as_dict = json.loads(r.text)
    measurement = queries.compareQueryResults(response_as_dict, testQuery)
    queryResults.append([testQuery, r, measurement])
    f.write(" => ".join([testQuery, r.text]))
    f.write("\n")
f.close()
# Safe the Querys with Results etc in a File for investigation later
f = open("testOutput.txt", "w")
for query in queryResults:
    f.write(str(query))
    f.write("\n")
f.close()


# Validate the Querys
successfull = 0
perfect = 0
own_failure = 0
server_failures = 0
testCount = 0

for queryResult in queryResults:
    testCount = testCount + 1
    if any(substring in queryResult[1].text for substring in ["GRAPHQL_PARSE_FAILED", "GRAPHQL_VALIDATION_FAILED"]):
        own_failure = own_failure + 1
    elif "INTERNAL_SERVER_ERROR" in queryResult[1].text or "error" in queryResult[1].text or queryResult[1].status_code == 500:
        server_failures = server_failures + 1
    elif "data" in queryResult[1].text and queryResult[2]["expectedPathLength"] > queryResult[2]["pathLengthFromResult"]:
        successfull = successfull + 1
    elif "data" in queryResult[1].text and queryResult[2]["expectedPathLength"] == queryResult[2]["pathLengthFromResult"]:
        perfect = perfect + 1

# Those with no failure
print("Good Tests: " + str(successfull))
# Those good tests that also have all the data as expected
print("Perfect Tests: " + str(perfect))
# Those with 400 Failure -> 400 induces that we did something wrong
print("Failed Tests cause of malformed Queries: " + str(own_failure))
# Those with 500 Failure -> 500 induces that server did something wrong
print("Confirmed Failed Tests: " + str(server_failures))
# overall Count
print("Tests overall: " + str(testCount))


# Graph zeichnen
nx.draw(graph, with_labels=True)
plt.show()