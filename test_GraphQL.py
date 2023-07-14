import requests
import queries
import json
import logging

def testQuery863b2fc0f9304c92af5f3c1eb58b2d93(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ character(id: \"YQBrlWbTAXpzwTMWwdPs\", ) {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ character(id: \"YQBrlWbTAXpzwTMWwdPs\", ) {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuerydb3dfc658b974d9e89e27f60e6d9918b(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ character(id: \"VqvhsmVYYTJSHYLznUvJ\", ) {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ character(id: \"VqvhsmVYYTJSHYLznUvJ\", ) {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuerye55b3aa3e0d2443b9326eefe9e780c6f(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ character(id: \"HQtkDCaecxxFOmuWxHmk\", ) {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ character(id: \"HQtkDCaecxxFOmuWxHmk\", ) {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery3919d036469044ae8d398ba899357e23(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ character(id: \"UsCTKwBaZzvxQtfrunnh\", ) {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ character(id: \"UsCTKwBaZzvxQtfrunnh\", ) {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuerya5efbab5dc19479781ef18fa896e19b8(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ character(id: \"SbgrzgeZpLjYYEtwiFfr\", ) {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ character(id: \"SbgrzgeZpLjYYEtwiFfr\", ) {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuerybcedfacffa1947af81ba75e38c301cca(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ character(id: \"DoZNqZohELBTKllCvGYC\", ) {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ character(id: \"DoZNqZohELBTKllCvGYC\", ) {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery05ac745e0aec4ecdb67ed9a22c42b938(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ character(id: \"uDDHBvciNddSElNTTJVn\", ) {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ character(id: \"uDDHBvciNddSElNTTJVn\", ) {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryaf934006cf634d8abe039b31b1e7e947(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ character(id: \"ZXQYMYhUChKxUlFoNyeu\", ) {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ character(id: \"ZXQYMYhUChKxUlFoNyeu\", ) {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery98ca6ce2f33a4541aa7bce272c67bcd8(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ character(id: \"JQxZGYhBeWLeGURDqqkr\", ) {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ character(id: \"JQxZGYhBeWLeGURDqqkr\", ) {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery9a72ec391b7e4748b2d5f3df32650a5f(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ character(id: \"oCLfXxPuKnTDVOiDVmUl\", ) {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ character(id: \"oCLfXxPuKnTDVOiDVmUl\", ) {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryc2fa7bab9c304211aee49cf760397ea3(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 5389, filter: {name: \"EdNMJOsZRnxtDxEkvEwX\",status: \"dfCuWJgSnSaQauREVYmN\",species: \"AvsJiRMiLQHRiTbWIofC\",type: \"eTGPrfWsdVDBqWCyERev\",gender: \"IvEusnJUUCzGHrIEbQZh\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 5389, filter: {name: \"EdNMJOsZRnxtDxEkvEwX\",status: \"dfCuWJgSnSaQauREVYmN\",species: \"AvsJiRMiLQHRiTbWIofC\",type: \"eTGPrfWsdVDBqWCyERev\",gender: \"IvEusnJUUCzGHrIEbQZh\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery336d8385cb034fe09cf3a648ff523a14(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 4028, filter: {name: \"nWnrdMAHXErhlPzdKPfv\",status: \"IVTJFZnexiIspGbrUVcg\",species: \"DKoiksKVcteIRePtzJRP\",type: \"KpNSiSRsZBmYXawYTCCA\",gender: \"VEHbTaFBIunNXiJCfCsv\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 4028, filter: {name: \"nWnrdMAHXErhlPzdKPfv\",status: \"IVTJFZnexiIspGbrUVcg\",species: \"DKoiksKVcteIRePtzJRP\",type: \"KpNSiSRsZBmYXawYTCCA\",gender: \"VEHbTaFBIunNXiJCfCsv\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryef0c5da2852e42aabb5194b46654a25d(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 1548, filter: {name: \"KodGsycmAzgmgUcWCstT\",status: \"TPEnFCLEsimnHrwFOPaA\",species: \"iwXuZxCdWyDmIiPMMByc\",type: \"JOaVQfDmfwHiwSYblFEM\",gender: \"CAiTOMlxckFIuMKXjgLB\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 1548, filter: {name: \"KodGsycmAzgmgUcWCstT\",status: \"TPEnFCLEsimnHrwFOPaA\",species: \"iwXuZxCdWyDmIiPMMByc\",type: \"JOaVQfDmfwHiwSYblFEM\",gender: \"CAiTOMlxckFIuMKXjgLB\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery8027d445e23e4985961e871ca98724b5(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 8586, filter: {name: \"hIGnmkxZOHEzzqPwibOb\",status: \"pnTifKoSfztHgQfoWKRB\",species: \"ZHLPOrqgSaGbdyvFpVGg\",type: \"rrgXPLEIlCiPzDwuUVuR\",gender: \"cxehSsiyWVGNJqVIibnq\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 8586, filter: {name: \"hIGnmkxZOHEzzqPwibOb\",status: \"pnTifKoSfztHgQfoWKRB\",species: \"ZHLPOrqgSaGbdyvFpVGg\",type: \"rrgXPLEIlCiPzDwuUVuR\",gender: \"cxehSsiyWVGNJqVIibnq\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery4baef16e57fc447e8ad1f6fb4227ceea(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 6768, filter: {name: \"LutRDYJszvYLOaKeauyy\",status: \"nmWcLGUmfgCpBKuVUlfR\",species: \"MvIhVbFunylsdqSBZald\",type: \"dmxhmaTVINlDsKkZzQMb\",gender: \"WYzEGmYaFEcYqVRJjxKY\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 6768, filter: {name: \"LutRDYJszvYLOaKeauyy\",status: \"nmWcLGUmfgCpBKuVUlfR\",species: \"MvIhVbFunylsdqSBZald\",type: \"dmxhmaTVINlDsKkZzQMb\",gender: \"WYzEGmYaFEcYqVRJjxKY\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuerydba3046cf92b446b97117dccd744e9d7(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 1778, filter: {name: \"wRTzxVDmUyCCCnMbbUna\",status: \"tXaDcRMrzdFUWMhLLEuZ\",species: \"QYJsnkWTxsHLDWZETMLw\",type: \"KVZGFkuzmgLseWvyDRow\",gender: \"pmnEJObjkPjtxTNHratV\",}, ) {   results {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 1778, filter: {name: \"wRTzxVDmUyCCCnMbbUna\",status: \"tXaDcRMrzdFUWMhLLEuZ\",species: \"QYJsnkWTxsHLDWZETMLw\",type: \"KVZGFkuzmgLseWvyDRow\",gender: \"pmnEJObjkPjtxTNHratV\",}, ) {   results {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryd8180440ac3342329f0ddd6c994bef46(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 7570, filter: {name: \"NqytXzRfeJFasjLMdtnu\",status: \"AwOHdUuWaLoncjpTYYHV\",species: \"HcctmpQuuHUsBijBTALm\",type: \"wGOoIYlWCcehxSqFqOaD\",gender: \"WvOtfYghjZTfsSuPnKqc\",}, ) {   results {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 7570, filter: {name: \"NqytXzRfeJFasjLMdtnu\",status: \"AwOHdUuWaLoncjpTYYHV\",species: \"HcctmpQuuHUsBijBTALm\",type: \"wGOoIYlWCcehxSqFqOaD\",gender: \"WvOtfYghjZTfsSuPnKqc\",}, ) {   results {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery7d8f71b544c4402194aa650dd0e0eba1(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 569, filter: {name: \"DZCyObMiamJEJDMbOUTR\",status: \"DXaiFTpioDoRcyYfBzuh\",species: \"BhMLzJEpbKMkzBhbQOSQ\",type: \"gFvqCUMZURnFSQYKhdhu\",gender: \"ZSGPAgtymOZKepZfKMjM\",}, ) {   results {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 569, filter: {name: \"DZCyObMiamJEJDMbOUTR\",status: \"DXaiFTpioDoRcyYfBzuh\",species: \"BhMLzJEpbKMkzBhbQOSQ\",type: \"gFvqCUMZURnFSQYKhdhu\",gender: \"ZSGPAgtymOZKepZfKMjM\",}, ) {   results {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryca756ac3a28a49868081f44d9fef3d1b(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 8743, filter: {name: \"uZFNrIWAKPewbAShmtBx\",status: \"NHWrnrgRkiqWrGbGhnrg\",species: \"yMmqYQizXnunTiZQnHID\",type: \"JcePlxcAgzdBqAohbvnA\",gender: \"nWCFZdigMoOwcIhPHKbF\",}, ) {   results {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 8743, filter: {name: \"uZFNrIWAKPewbAShmtBx\",status: \"NHWrnrgRkiqWrGbGhnrg\",species: \"yMmqYQizXnunTiZQnHID\",type: \"JcePlxcAgzdBqAohbvnA\",gender: \"nWCFZdigMoOwcIhPHKbF\",}, ) {   results {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery9f7e8481fc2d4ea386f95b83ef9fe301(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 5266, filter: {name: \"GdafuTIMxBgcqGyZnuxQ\",status: \"KkrWpoUysVVLvgrwSWRf\",species: \"CuvvigwcKqHIUHglqTbF\",type: \"RfdGMhOGuroqmJMkLnoK\",gender: \"zTmDdjnKhhBRpXORvOCZ\",}, ) {   results {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 5266, filter: {name: \"GdafuTIMxBgcqGyZnuxQ\",status: \"KkrWpoUysVVLvgrwSWRf\",species: \"CuvvigwcKqHIUHglqTbF\",type: \"RfdGMhOGuroqmJMkLnoK\",gender: \"zTmDdjnKhhBRpXORvOCZ\",}, ) {   results {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery2c09f727c9ba41a18f1ac3ceb36d5728(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 3113, filter: {name: \"DFnAEIjAgJpLRRGagFcb\",status: \"gmEOoNVwwQHocAwJHTix\",species: \"ALGdSsZtNcqFklFbEnhv\",type: \"QkbKfTcbAEyfZrZwqzEs\",gender: \"jYEDlSZyNNVqNjyLAcfW\",}, ) {   results {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 3113, filter: {name: \"DFnAEIjAgJpLRRGagFcb\",status: \"gmEOoNVwwQHocAwJHTix\",species: \"ALGdSsZtNcqFklFbEnhv\",type: \"QkbKfTcbAEyfZrZwqzEs\",gender: \"jYEDlSZyNNVqNjyLAcfW\",}, ) {   results {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery6ef80027d2b545c6b5e8025a7ed8ece9(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 8913, filter: {name: \"nzyVgSNtbkDOSLPYHlCV\",status: \"xHXyoNITGLKKftSyFeQg\",species: \"QFmwsELInriarJkRsIJY\",type: \"UsFpLHvVuWCowgQhRMXb\",gender: \"faTuYxNwncbQwdZGImgw\",}, ) {   results {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 8913, filter: {name: \"nzyVgSNtbkDOSLPYHlCV\",status: \"xHXyoNITGLKKftSyFeQg\",species: \"QFmwsELInriarJkRsIJY\",type: \"UsFpLHvVuWCowgQhRMXb\",gender: \"faTuYxNwncbQwdZGImgw\",}, ) {   results {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryef3d7c0a3674429e810d9983deddd28c(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 2281, filter: {name: \"bZKtccZkDLMjfmxXXiGJ\",status: \"aigZsdufUUetaezREnBc\",species: \"exKJvVHwZhFmyVWFgjUc\",type: \"eIjMzZkFDeWZeZnWRKaz\",gender: \"KnXnHZfREmeREtMVTgYb\",}, ) {   results {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 2281, filter: {name: \"bZKtccZkDLMjfmxXXiGJ\",status: \"aigZsdufUUetaezREnBc\",species: \"exKJvVHwZhFmyVWFgjUc\",type: \"eIjMzZkFDeWZeZnWRKaz\",gender: \"KnXnHZfREmeREtMVTgYb\",}, ) {   results {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery0c796afee541432c9c7f00fae5c48a9a(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 1572, filter: {name: \"sVNeVCAUEemCBHVwkSjN\",status: \"DWSfbpXybEazUHoYggUU\",species: \"hyOkHVJBOHvgFDwvVkNK\",type: \"qVtEEETCIXCEiNQQWcUy\",gender: \"AVsHitxkiOVagyPosfAM\",}, ) {   results {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 1572, filter: {name: \"sVNeVCAUEemCBHVwkSjN\",status: \"DWSfbpXybEazUHoYggUU\",species: \"hyOkHVJBOHvgFDwvVkNK\",type: \"qVtEEETCIXCEiNQQWcUy\",gender: \"AVsHitxkiOVagyPosfAM\",}, ) {   results {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery64c9434d3d6a427586f40626feb1d351(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ characters(page: 2108, filter: {name: \"kmmRzjNVilXeshpcasqn\",status: \"JVpuheLsSuAzAPIBbLBf\",species: \"LoGzQYkELEvxaoboesTp\",type: \"tqAIcftQLaURiemWGWsL\",gender: \"PqarXfvQchdrrUVTyzcg\",}, ) {   results {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ characters(page: 2108, filter: {name: \"kmmRzjNVilXeshpcasqn\",status: \"JVpuheLsSuAzAPIBbLBf\",species: \"LoGzQYkELEvxaoboesTp\",type: \"tqAIcftQLaURiemWGWsL\",gender: \"PqarXfvQchdrrUVTyzcg\",}, ) {   results {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuerydcffc432c3c4496d89bb8cbacbc39485(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ location(id: \"ABspFelMsPcbBPVaHddD\", ) {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ location(id: \"ABspFelMsPcbBPVaHddD\", ) {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery859bb7354a48466482e653399b624e29(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ location(id: \"mBTrPsegsCpYLugxSDSC\", ) {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ location(id: \"mBTrPsegsCpYLugxSDSC\", ) {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryaf74bd4bb01c463db67ec5fe162f15f5(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ location(id: \"SebbYfNXtrQBeiDgIOdJ\", ) {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ location(id: \"SebbYfNXtrQBeiDgIOdJ\", ) {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery4873a4d23e794f7987e642c8295ee656(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ location(id: \"tKhjvZbspoNORZuktNzz\", ) {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ location(id: \"tKhjvZbspoNORZuktNzz\", ) {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryd5aec9682eb04630b5f4b5f87a7b4cf5(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ location(id: \"KnWXrRMcAtqLdoVMQRdU\", ) {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ location(id: \"KnWXrRMcAtqLdoVMQRdU\", ) {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryffd65484b29b42b5a8f3e7766fdc83c4(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ locations(page: 3074, filter: {name: \"UxYonCNUSzZDFoByXgww\",type: \"RAHKHGJtGkRaAcoDmnct\",dimension: \"DnqxMTuUWiEEfbTLRAFP\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ locations(page: 3074, filter: {name: \"UxYonCNUSzZDFoByXgww\",type: \"RAHKHGJtGkRaAcoDmnct\",dimension: \"DnqxMTuUWiEEfbTLRAFP\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery73bf8ca9a3ba452aa95d6db2412f7fbb(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ locations(page: 6918, filter: {name: \"obpImGklzBgqafSAYySc\",type: \"CXcfHRNlDOQXcrUMuCpX\",dimension: \"XNzJRbnhofAlVisgrmjZ\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ locations(page: 6918, filter: {name: \"obpImGklzBgqafSAYySc\",type: \"CXcfHRNlDOQXcrUMuCpX\",dimension: \"XNzJRbnhofAlVisgrmjZ\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery572978e6232944baa1298adc36572c70(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ locations(page: 8615, filter: {name: \"UnVHakFokyGAlRibtVCr\",type: \"DAJtowSMdBfdoiXjjJsZ\",dimension: \"kUcQmccpXjcSyUoWXjzU\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ locations(page: 8615, filter: {name: \"UnVHakFokyGAlRibtVCr\",type: \"DAJtowSMdBfdoiXjjJsZ\",dimension: \"kUcQmccpXjcSyUoWXjzU\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery4b59470e048f4285aa369358fa930634(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ locations(page: 8567, filter: {name: \"QKXZuEMJfdlIBnIASptR\",type: \"feSbpEifFuVmHhrXwkAw\",dimension: \"tKdAjDymbiFnNPAqTUTe\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ locations(page: 8567, filter: {name: \"QKXZuEMJfdlIBnIASptR\",type: \"feSbpEifFuVmHhrXwkAw\",dimension: \"tKdAjDymbiFnNPAqTUTe\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryfcbd3e0654e64c5ab4a208a43f2f876f(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ locations(page: 8869, filter: {name: \"lLLHhjjzQOSWjnFBgvpB\",type: \"ZOvhOhGuTaMWIiSjwtqa\",dimension: \"BrRjBzcXXkGnwFWGMLpx\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ locations(page: 8869, filter: {name: \"lLLHhjjzQOSWjnFBgvpB\",type: \"ZOvhOhGuTaMWIiSjwtqa\",dimension: \"BrRjBzcXXkGnwFWGMLpx\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryfccc16cacc4844dc849cfd88b881ff3a(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ locations(page: 7729, filter: {name: \"xGFKQDOwYpdOfRxYYHFH\",type: \"EfnQfZBviNDuvesKPXGJ\",dimension: \"jyZbAQTcCJdTvMplXafw\",}, ) {   results {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ locations(page: 7729, filter: {name: \"xGFKQDOwYpdOfRxYYHFH\",type: \"EfnQfZBviNDuvesKPXGJ\",dimension: \"jyZbAQTcCJdTvMplXafw\",}, ) {   results {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryac47a8be6af44b6fb89a872aea3c3b25(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ locations(page: 529, filter: {name: \"YDzitTbySTwzBBhwbsLS\",type: \"xCUEsoUHBdQBZcMyzfMs\",dimension: \"qLISLRfvaULkdEQgLGHq\",}, ) {   results {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ locations(page: 529, filter: {name: \"YDzitTbySTwzBBhwbsLS\",type: \"xCUEsoUHBdQBZcMyzfMs\",dimension: \"qLISLRfvaULkdEQgLGHq\",}, ) {   results {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery611411f6fae04cbb8ad500e703ced339(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ locations(page: 3488, filter: {name: \"rkdPATTXweJoqqGMqGng\",type: \"tKVhKtIVrhUmqfpHAErb\",dimension: \"DNdxTUYDcUtLqDtEugXf\",}, ) {   results {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ locations(page: 3488, filter: {name: \"rkdPATTXweJoqqGMqGng\",type: \"tKVhKtIVrhUmqfpHAErb\",dimension: \"DNdxTUYDcUtLqDtEugXf\",}, ) {   results {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuerye401a16f14c9485c8e8c21efb6e9b7af(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ locations(page: 304, filter: {name: \"CUZssdiCTWwEXUpKiIyS\",type: \"UKFALCRyRdgezUONUhYj\",dimension: \"gOeDSjMaddeTyxPFbnwW\",}, ) {   results {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ locations(page: 304, filter: {name: \"CUZssdiCTWwEXUpKiIyS\",type: \"UKFALCRyRdgezUONUhYj\",dimension: \"gOeDSjMaddeTyxPFbnwW\",}, ) {   results {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery3696453fdf7c40ef97bd2179247078d6(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ locations(page: 5576, filter: {name: \"WCvzwGsfUlbAomUtltLo\",type: \"XINVIfIGUDcYWKPxUlzb\",dimension: \"wAOrDHyoaPyozOdxUlKv\",}, ) {   results {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ locations(page: 5576, filter: {name: \"WCvzwGsfUlbAomUtltLo\",type: \"XINVIfIGUDcYWKPxUlzb\",dimension: \"wAOrDHyoaPyozOdxUlKv\",}, ) {   results {  id  name  type  dimension  created   residents {  id  name  status  species  type  gender  image  created   episode {  id  name  air_date  episode  created   }  }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery4210b2efb51f455eb952ca6b1e40edc8(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episode(id: \"svpslfUVnquvtUuJPVoV\", ) {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episode(id: \"svpslfUVnquvtUuJPVoV\", ) {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryf2365b20c93a46b997fe24b56b28284c(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episode(id: \"yJDPsvNFSHSlhjdCFOSh\", ) {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episode(id: \"yJDPsvNFSHSlhjdCFOSh\", ) {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery3cbe241677bd42c392398f2e59eb920b(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episode(id: \"OvPBbYNodgvVywLcvZPj\", ) {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episode(id: \"OvPBbYNodgvVywLcvZPj\", ) {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery3058e2b6007c4efa90588f23cdbe4d7c(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episode(id: \"uFhoUrVaTPStjgYrxVTt\", ) {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episode(id: \"uFhoUrVaTPStjgYrxVTt\", ) {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery4907a9f717754757a49c2129b23bd312(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episode(id: \"JJxSBujCBiinXIjTcGyu\", ) {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episode(id: \"JJxSBujCBiinXIjTcGyu\", ) {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery223cbf67e7de4f019d3efd0a438e7420(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episodes(page: 6725, filter: {name: \"fdLJYcrOdkSUegZmdcsb\",episode: \"vOTPmfjuMwoiZanJwelF\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episodes(page: 6725, filter: {name: \"fdLJYcrOdkSUegZmdcsb\",episode: \"vOTPmfjuMwoiZanJwelF\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery65763d2f45d440bea4cc52b003500974(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episodes(page: 7755, filter: {name: \"rkWbuxsLNWCDWDhmGtwO\",episode: \"FkWjEzgvGOjmKAGrjhtg\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episodes(page: 7755, filter: {name: \"rkWbuxsLNWCDWDhmGtwO\",episode: \"FkWjEzgvGOjmKAGrjhtg\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery82209104829a45aa8d0ae8322db192f3(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episodes(page: 2741, filter: {name: \"ftXnfxKIeolmJamczxMG\",episode: \"qnxaNwXazYIsEkzTToba\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episodes(page: 2741, filter: {name: \"ftXnfxKIeolmJamczxMG\",episode: \"qnxaNwXazYIsEkzTToba\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery8e6b73bdff7d42eaa111e34a18dba016(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episodes(page: 586, filter: {name: \"UnTQQsDtuvFEXGQUkvZV\",episode: \"scfxmCmTAULdpopBHpgL\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episodes(page: 586, filter: {name: \"UnTQQsDtuvFEXGQUkvZV\",episode: \"scfxmCmTAULdpopBHpgL\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery1dccb01c29d24670a09a35054795c70c(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episodes(page: 5431, filter: {name: \"bOhcwVHiXCAZJEToUPsk\",episode: \"pyOyloeDWOKnGIhLQwLg\",}, ) {   info {  count  pages  next  prev   }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episodes(page: 5431, filter: {name: \"bOhcwVHiXCAZJEToUPsk\",episode: \"pyOyloeDWOKnGIhLQwLg\",}, ) {   info {  count  pages  next  prev   }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery745dad4529184747921ec0350046e5e5(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episodes(page: 8924, filter: {name: \"ziLlerLZzhKNqQCOsoTb\",episode: \"SZpFPbJILkwMtTxDhRrw\",}, ) {   results {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episodes(page: 8924, filter: {name: \"ziLlerLZzhKNqQCOsoTb\",episode: \"SZpFPbJILkwMtTxDhRrw\",}, ) {   results {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQueryb7c0fb9a872b4ef1baa5d326a39c5df4(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episodes(page: 8181, filter: {name: \"xGIolEEPrVRnVUHOapFG\",episode: \"LaOvlclMsPGlHtHwbEEr\",}, ) {   results {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episodes(page: 8181, filter: {name: \"xGIolEEPrVRnVUHOapFG\",episode: \"LaOvlclMsPGlHtHwbEEr\",}, ) {   results {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery5ead6b50a47f47488fc1758ab7d1e17b(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episodes(page: 5939, filter: {name: \"GIbpRlweUvnekhBRUKty\",episode: \"YQayvQVounzLQckoLEQB\",}, ) {   results {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episodes(page: 5939, filter: {name: \"GIbpRlweUvnekhBRUKty\",episode: \"YQayvQVounzLQckoLEQB\",}, ) {   results {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery4693d80bf7b84d61a9d3e227c57ad8a1(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episodes(page: 6142, filter: {name: \"eWRCOANpzdDvCTplZbpY\",episode: \"WukCyoIrekaBbNpKmrXa\",}, ) {   results {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episodes(page: 6142, filter: {name: \"eWRCOANpzdDvCTplZbpY\",episode: \"WukCyoIrekaBbNpKmrXa\",}, ) {   results {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


def testQuery4d5fe676a53147c18f5599bd30154987(caplog):
    caplog.set_level(logging.WARNING)
    response = requests.post("https://rickandmortyapi.com/graphql",json={'query':"{ episodes(page: 980, filter: {name: \"vRTdYLTsVqbkpGRrOGKM\",episode: \"BlWXvodJETLVUCYpXCme\",}, ) {   results {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }  }"})
    response_as_dict = json.loads(response.text)
    measurement = queries.compareQueryResults(response_as_dict, "{ episodes(page: 980, filter: {name: \"vRTdYLTsVqbkpGRrOGKM\",episode: \"BlWXvodJETLVUCYpXCme\",}, ) {   results {  id  name  air_date  episode  created   characters {  id  name  status  species  type  gender  image  created   origin {  id  name  type  dimension  created   }  }  }  }  }")
    if measurement["expectedPathLength"] > measurement["pathLengthFromResult"]:
        logging.warning(" Test hat nicht 100% Abdeckung ")
    assert response.status_code == 200


