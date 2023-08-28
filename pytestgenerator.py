import uuid


def generateTestFromQuery(testQuery, url):
    testQueryAsValidString = testQuery.replace('"', '\\"')
    testString = "def testQuery" + str(uuid.uuid4()).replace('-', '') + "(caplog):" + "\n"
    testString = testString + "    caplog.set_level(logging.WARNING)" + "\n"
    testString = testString + "    response = requests.post(\"" + url + "\"," "json={\'query\':\"" + testQueryAsValidString + "\"})" + "\n"
    testString = testString + "    response_as_dict = json.loads(response.text)"  + "\n"
    testString = testString + "    measurement = queries.compareQueryResults(response_as_dict, " + "\"" + testQueryAsValidString + "\"" + ")" + "\n"
    testString = testString + "    if measurement[\"expectedPathLength\"] > measurement[\"pathLengthFromResult\"]:" + "\n"
    testString = testString + "        logging.warning(\" Test hat nicht 100% Abdeckung \")" + "\n"
    testString = testString + "    assert response.status_code == 200" + "\n"
    testString = testString + "\n" + "\n"
    return testString
