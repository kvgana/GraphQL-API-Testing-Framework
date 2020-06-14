import requests
import json
from sgqlc.endpoint.http import HTTPEndpoint
import jsonschema
import os
from gql_query_builder import GqlQuery
from assertpy import assert_that

#Endpoint
URL = "https://traveller-core.dev.pelago.co/graphql"

# Product query builder
dataSet1 = ['productId', 'productName', 'mediaLinks', 'cancellationType', 'cancellationCutoff', 'minGroupSize', 'duration']
dataSet2 = ['destinationId', 'openDateTicket', 'collectPhysicalTicket', 'confirmationType' , 'voucherType', 'guideLanguage']
dataSet3 = ['priceRangeFrom', 'priceRangeTo', 'priceAdultFrom', 'priceChildFrom', 'latitude', 'longitude', 'address', 'content']
dataSet = dataSet1 + dataSet2 + dataSet3
product_query = GqlQuery().fields(dataSet).query('product', input={"productId": '"pgfnl"'}).operation().generate()

INVALID_LOGIN_MUTATION = """mutation {
   login(email: "ytest@gmail.com",  password: "hope"){
    accessToken
  }
}"""


def test_mutation_invalid_login():
  #Build Mutation and make a post call to Graphql API over https
  response = requests.post(URL, json={'query': INVALID_LOGIN_MUTATION})

  #Print response code
  print(response.status_code)
  print("Invalid login Mutation response code = " + str(response.status_code))
  print("Response content is " + str(response.content))

  #Verify the response and error message
  assert_that(response.status_code).is_equal_to(200)
  response_content = json.loads(response.content)
  response_message = (response_content.get('errors')[0].get('message'))
  assert_that(response_message).is_equal_to("Invalid Credentials")


def test_query_product():
  #Fetch the schema file and load the schema
  THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
  file = os.path.join(THIS_FOLDER, 'response_schema.json')
  with open(file, 'r') as f:
    schema_data = f.read()
  schema = json.loads(schema_data)

  #Build Query and make a post call to Graphql API over https
  response = requests.post(URL, json={'query': product_query})

  #Verify the response code
  print("Product query response code = " + str(response.status_code))
  assert_that(response.status_code).is_equal_to(200)

  #Validate the response schema with expected schema
  json_response = json.loads(response.text)
  jsonschema.validate(json_response, schema)
