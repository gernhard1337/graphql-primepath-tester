# fremde Imports
import matplotlib.pyplot as plt
import networkx as nx
import json
import requests
# eigene Imports
import queries
import datagenerator
import graphhandler
import querygenerator

# testUrls die funktionieren sollten
# https://rickandmortyapi.com/graphql -> works
# https://countries.trevorblades.com/graphql -> works but not in fullest
#
# http://localhost:4000/graphql -> run minimaltestServer2.js, all works
testUrl = "https://rickandmortyapi.com/graphql"
testPerPath = 5
# Schema Query
r = requests.post(testUrl, json={'query': queries.introspection_query})
json_data = json.loads(r.text)
with open('data.json', 'w') as f:
    json.dump(json_data, f)

# Graph aus Query
graph = nx.DiGraph()
type_dict = {gqltype['name']: gqltype for gqltype in json_data['data']['__schema']['types']}

with open('dict.json', "w") as f:
    json.dump(type_dict, f)

# PrimePaths finden - change method for other coverage if wanted
graphhandler.buildGraph(graph, "Query", type_dict)
print(graph.edges("Query"))
primePaths = graphhandler.findPrimePaths_withFilter("Query", graph)

# experimentell mal noch andere Pfade die andere Kriterien umsetzen hinzufügen
#for path in graphhandler.findCompletePathCoverage("Query", graph):
#    primePaths.append(path)
#for path in graphhandler.findNodeCoveragePaths("Query", graph):
#    primePaths.append(path)
#for path in graphhandler.findEdgeCoveragePaths("Query", graph):
#    primePaths.append(path)


# PrimePaths zu Query
primePathQueries = []
for primePath in primePaths:
    # 5 Tests pro Pfad
    for x in range(testPerPath):
        primePathQueries.append(querygenerator.pathToQuery(primePath, type_dict, graph))

# Run the Querys
queryResults = []
for testQuery in primePathQueries:
    print(testQuery)
    r = requests.post(testUrl, json={'query': testQuery})
    response_as_dict = json.loads(r.text)
    measurement = queries.compareQueryResults(response_as_dict, testQuery)
    print(measurement)
    queryResults.append([testQuery, r, measurement])

# Safe the Querys with Results etc in a File for investigation later
f = open("testOutput.txt", "w")
for query in queryResults:
    f.write(str(query))
    f.write("\n")
f.close()


# Validate the Querys
successfull = 0
own_failure = 0
server_failures = 0
testCount = 0
for queryResult in queryResults:
    testCount = testCount + 1
    if any(substring in queryResult[1].text for substring in ["GRAPHQL_PARSE_FAILED", "GRAPHQL_VALIDATION_FAILED"]):
        own_failure = own_failure + 1
    elif "INTERNAL_SERVER_ERROR" in queryResult[1].text:
        server_failures = server_failures + 1
    elif "data" in queryResult[1].text:
        successfull = successfull + 1

# Those with no failure
print("Good Tests: " + str(successfull))
# Those good tests that also have all the data as expected
print("Perfect Tests: ")
# Those with 400 Failure -> 400 induces that we did something wrong
print("Own Failures from Tool Tests: " + str(own_failure))
# Those with 500 Failure -> 500 induces that server did something wrong
print("Confirmed Failed Tests: " + str(server_failures))
# overall Count
print("Tests overall: " + str(testCount))


# Graph zeichnen
nx.draw(graph, with_labels=True)
plt.show()


