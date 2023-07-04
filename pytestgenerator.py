import uuid


def generateTestFromQuery(testQuery, url):
    testQueryAsValidString = testQuery.replace('"', '\\"')
    testString = "def testQuery" + str(uuid.uuid4()).replace('-', '') + "():" + "\n"
    testString = testString + "    response = requests.post(\"" + url + "\"," "json={\'query\':\"" + testQueryAsValidString + "\"})" + "\n"
    testString = testString + "    assert response.status_code == 200" + "\n"
    testString = testString + "\n" + "\n"
    return testString
