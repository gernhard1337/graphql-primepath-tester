import requests

def testQuery263d8495a61c40f28856fdcce4863f4f():
    response = requests.post("http://localhost:4000/graphql",json={'query':"{ project(id: \"vuBnvzlrIkNMBAvBzcIJ\", ) {  id  name  description   owner {  id  name  age   }  }  }"})
    assert response.status_code == 200


def testQuery9426abd6af5d4c17abb58d24d2dc8a1a():
    response = requests.post("http://localhost:4000/graphql",json={'query':"{ project(id: \"EYzTPCzzDjHAcCMOOLPd\", ) {  id  name  description   owner {  id  name  age   }  }  }"})
    assert response.status_code == 200


def testQuerye4472259278a4d8fb99201be17d85074():
    response = requests.post("http://localhost:4000/graphql",json={'query':"{ project(id: \"PXVxzZOHBkrwFRMNIChb\", ) {  id  name  description   owner {  id  name  age   }  }  }"})
    assert response.status_code == 200


def testQuery80224404fe7c4f68953f41a8adacde59():
    response = requests.post("http://localhost:4000/graphql",json={'query':"{ project(id: \"LgrLfEoLxMgexMIHMOfO\", ) {  id  name  description   owner {  id  name  age   }  }  }"})
    assert response.status_code == 200


def testQuery7c0f5022f21148d7a95dfce2dc8325b0():
    response = requests.post("http://localhost:4000/graphql",json={'query':"{ project(id: \"hgwGsOXkIXOLNjGQpZDZ\", ) {  id  name  description   owner {  id  name  age   }  }  }"})
    assert response.status_code == 200


