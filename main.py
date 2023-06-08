# fremde Imports
import matplotlib.pyplot as plt
import networkx as nx
import json
import requests
# eigene Imports
import queries
import datagenerator
import pathfinder

testUrl = "http://localhost:4000/graphql"

# Abfrage zur Introspektion des Schemas
introspection_query = """
    query IntrospectionQuery {
  __schema {
    queryType {
      name
    }
    mutationType {
      name
    }
    subscriptionType {
      name
    }
    types {
      ...FullType
    }
    directives {
      name
      description
      locations
      args {
        ...InputValue
      }
    }
  }
}

fragment FullType on __Type {
  kind
  name
  description
  fields(includeDeprecated: true) {
    name
    description
    args {
      ...InputValue
    }
    type {
      ...TypeRef
    }
    isDeprecated
    deprecationReason
  }
  inputFields {
    ...InputValue
  }
  interfaces {
    ...TypeRef
  }
  enumValues(includeDeprecated: true) {
    name
    description
    isDeprecated
    deprecationReason
  }
  possibleTypes {
    ...TypeRef
  }
}

fragment InputValue on __InputValue {
  name
  description
  type {
    ...TypeRef
  }
  defaultValue
}

fragment TypeRef on __Type {
  kind
  name
  ofType {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
              }
            }
          }
        }
      }
    }
  }
}
"""

# Ausführen der Schema-Abfrage
r = requests.post(testUrl, json={'query': introspection_query})
json_data = json.loads(r.text)
with open('data.json', 'w') as f:
    json.dump(json_data, f)

# Erstellen Sie ein NetworkX-Graph aus dem GraphQL-Schema
graph = nx.DiGraph()

baseDatatypes = ["Boolean", "String", "ID", "Int", "Date", "Float"]
nonSchemaTypePrefix = "__"

def add_edges(graph, type_name, type_dict):
    if type_name.startswith(nonSchemaTypePrefix) or type_name in baseDatatypes:
        return
    else:
        for adjacentNode in type_dict[type_name]['fields']:
            if graph.has_edge(adjacentNode['type']['name'], type_name):
                return
            else:
                if adjacentNode['type']['name']:
                    graph.add_edge(type_name, adjacentNode['type']['name'])
                    add_edges(graph, adjacentNode['type']['name'], type_dict)
                if adjacentNode['type']['kind'] == 'LIST':
                    graph.add_edge(type_name, adjacentNode['type']['ofType']['name'])
                    add_edges(graph, adjacentNode['type']['ofType']['name'], type_dict)

type_dict = {gqltype['name']: gqltype for gqltype in json_data['data']['__schema']['types']}

with open('dict.json', "w") as f:
    json.dump(type_dict, f)

add_edges(graph, "Query", type_dict)

def find_prime_paths(graph, start_node):
    return []





start_node = "Query"
prime_paths = find_prime_paths(graph, start_node)

for path in prime_paths:
    print(path)



nx.draw(graph, with_labels=True)
plt.show()


