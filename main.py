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
# https://rickandmortyapi.com/graphql
# https://countries.trevorblades.com/graphql
# https://beta.pokeapi.co/graphql/v1beta
#
#
# http://localhost:4000/graphql -> run minimaltestServer2.js
testUrl = "http://localhost:4000/graphql"

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

# PrimePaths finden
graphhandler.buildGraph(graph, "Query", type_dict)
primePaths = graphhandler.findPrimePaths("Query", graph)

# PrimePaths zu Query
primePathQueries = []
for primePath in primePaths:
    primePathQueries.append(querygenerator.pathToQuery(primePath, type_dict, graph))

print(primePathQueries)

# Run the Querys
queryResults = []
for testQuery in primePathQueries:
    r = requests.post(testUrl, json={'query': testQuery})
    queryResults.append([testQuery, r])

# Validate the Querys
successfull = 0
own_failure = 0
server_failures = 0
testCount = 0
for queryResult in queryResults:
    testCount = testCount + 1
    if "data" in queryResult[1].text:
        successfull = successfull + 1
    if "GRAPHQL_VALIDATION_FAILED" in queryResult[1].text:
        own_failure = own_failure + 1
    if "INTERNAL_SERVER_ERROR" in queryResult[1].text:
        server_failures = server_failures + 1

print("Good Tests: " + str(successfull))
print("Wrong Tests: " + str(own_failure))
print("Failed Tests: " + str(server_failures))
print("Tests overall: " + str(testCount))




# Graph zeichnen
nx.draw(graph, with_labels=True)
plt.show()


