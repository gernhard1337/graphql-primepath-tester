How to run: 
# Install Python
    - depending on your system

# Install Dependencies 
    - pip install matplotlib networkx json requests faker pytest uuid
    or 
    - pip3 install matplotlib networkx json requests faker pytest uuid
# Run
    - python main.py API-URL TEST-COUNT
Replace the API-URL with the Url you want to test. Otherwise there is a default URL defined.
Replace TEST-COUNT with the tests that shall be generated per path. Default is 5 tests per path
There are several Coveragecriterias implemented, one can change the algorithm used for 
path generation by changing the line:
    `paths = graphhandler.generate_prime_paths_2("Query", graph)`


# Change default Url (optional)
    - line 17. in main.py

# Conditions
    - Your GraphQL API-Endpoint needes to allow a introspection query + no depth limit. 

# Tool-Output
The Tool will Output the exact Error-Message your Server returned via GraphQL.
It will print the query that created the error so you can investigate what leads to the failures.

The Last Output will be some Statistics:
- Good Tests is the amount of tests, that succeeded but without actually testing all due to lack of precisnes in input data. (Result Pathlength != Expected Pathlength)
- Perfect Tests are tests that succeeded but actually have met the Condition (Result Pathlength == Expected Pathlength). 
- "Failed Tests cause of malformed Queries" are failed tests but the reason is due to failure in test generation. Those are false positives
- Confirmed Failed Tests are the tests that are actually Wrong and need investigation due to failures in the code! 
- Test overall is just a measurement how much tests got created as whole

The Tool will also output a file test_GraphQL.py
Those are unit-tests for pytest. 
Run `pytest` in root of project when the file is existing to run the tests.