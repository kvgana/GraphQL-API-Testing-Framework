**Pelago Challenge**

**Description**
This mini project is a Python based Testing framework for GraphQL 
API over HTTP, using Pytest, Gql_query_builder and Assertpy. Contains a few automated tests  and
a list of other testcases(tescase.suite)

**Getting Started**
The below setup instructions are in reference to Mac OS.(and Equivalent commands for Linux)

**Pre-requisites**
Python3 (version: 3.7.7)
pytest(version >5.0)
pip -  Python Package Manager (python get-pip.py)

**Libraries to install**
The below libraries can be installed using pip(pip install <name>) or from 'Project Interpreter'
'pytest' - Testing framework. Can be used for enhancing tests for DB validation and UI tests
'requests' - To make Graphql API calls over HTTP - 
'json' and 'jsonschema' - To perform json and json files related operations
'gql_query_builder' - To build Query, Mutation with ease
'assertpy' - Assertion library

**Running the tests**
Download the repo from Github
Open the 'pelago' folder
Move to 'tests' folder
To directly run the file - Run 'test_sanity.py'
To run from command line - 
  pytest                    -> Runs all the tests under tests folder
  pytest -s                 -> Runs the tests and prints to console 
  pytest -n <threads_count> -> Runs tests parallely with mentioned threads_count

List of testcase for the graphql/product endpoint is added in 'testcaseSuite' file

**Architecture**
Why Python?
After looking over the Javascript, Apollo test client and Python languages suitability to build a test framework for GrapghQl,
Python has advantages as list below - 

1. Suitability to extend to DB validation tests and even UI tests
2. Large open source community
3. Support for GraphQL API testing from building queries to Snapshot testing
4. Large number of updates on libraries
5. Easy to understand syntax, setup and maintainability

Why Pytest?
1. Pytest testing framework provides well defined testcase structure.
2. Supports parallel testing
3. Compatible with assertion libraries and others 
4. Coupled with Python official base

Aspects to can be extended - 
1. Maintaining config files for different environments
2. Consumers to build Queries/Mutations
3. Validation utilities to abstract validations from tests 
4. GraphQL Fragments to implement DRY when testcase combinations increase
5. Parameterising testcases 
6. Reporting tool like Allure to understand reports faster when included in CI/CD
 (1, 2, 3 are trade-offs done due to time constraints)
 
Framework can support the below types of testing -
1. Snapshot testing - To keep track of changes in response as APIs evolve. Hence report bugs early.
2. Load testing - To perform Load testing using graphql-client 
3. Mocking DB data - Using graphql-tools, useful to speed up testing when dev work is
   in progress and even reduce the load on DB.
 

