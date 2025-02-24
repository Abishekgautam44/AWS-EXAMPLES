# AWS API GATEWAY

## Creating the first API endpoint (GET)

```sh
import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')

response = client.create_rest_api(
    name='ProductsApi',
    description='API to get all the food products.',
    minimumCompressionSize=123,
    endpointConfiguration={
        'types': [
            'REGIONAL',
        ]
    }
)
api_id = response["id"]

resources = client.get_resources(restApiId=api_id)
root_id = [resource for resource in resources["items"] if resource["path"] == "/"][0]["id"]

products = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='products'
)
products_resource_id = products["id"]


product_method = client.put_method(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

product_response = client.put_method_response(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': True,
        'method.response.header.Access-Control-Allow-Origin': True,
        'method.response.header.Access-Control-Allow-Methods': True
    },
    responseModels={
        'application/json': 'Empty'
    }
)

product_integration = client.put_integration(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)


product_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseTemplates={
        "application/json": json.dumps({
            "product_item_arr": [
                {
                    "product_name_str": "apple pie slice",
                    "product_id_str": "a444",
                    "price_in_cents_int": 595,
                    "description_str":"amazing taste",
                    "tag_str_arr": ["pie slice","on offer"],
                    "special_int": 1
                },{
                    "product_name_str": "chocolate cake slice",
                    "product_id_str": "a445",
                    "price_in_cents_int": 595,
                    "description_str":"chocolate heaven",
                    "tag_str_arr": ["cake slice","on offer"]
                },{
                    "product_name_str": "chocolate cake",
                    "product_id_str": "a446",
                    "price_in_cents_int": 4095,
                    "description_str": "chocolate heaven",
                    "tag_str_arr": ["whole cake", "on offer"]
                }
            ]
        })
    },
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        'method.response.header.Access-Control-Allow-Methods': "'GET'",
        'method.response.header.Access-Control-Allow-Origin': "'*'"
    }
)


print ("DONE")

```
## Creating the second API endpoint (GET)
```sh
import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')


api_id = 'b6prjz6zv3'
parent_id = 'unqbup'

products = client.create_resource(
    restApiId=api_id,
    parentId=parent_id,
    pathPart='on_offer'
)
products_resource_id = products["id"]


product_method = client.put_method(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

product_response = client.put_method_response(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': True,
        'method.response.header.Access-Control-Allow-Origin': True,
        'method.response.header.Access-Control-Allow-Methods': True
    },
    responseModels={
        'application/json': 'Empty'
    }
)

product_integration = client.put_integration(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)


product_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseTemplates={
        "application/json": json.dumps({
            "product_item_arr": [{
                "product_name_str": "apple pie slice",
                "product_id_str": "a444",
                "price_in_cents_int": 595,
                "description_str": "amazing taste",
                "tag_str_arr": [
                  "pie slice",
                  "on offer"
                ],
                "special_int": 1
              }]
        })
    },
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        'method.response.header.Access-Control-Allow-Methods': "'GET'",
        'method.response.header.Access-Control-Allow-Origin': "'*'"
    }
)


print ("DONE")
```
## Creating the third API endpoing (POST)

### Finding out the api_id

```sh
aws apigateway get-rest-apis --query items[0].id --output text
```

```sh
import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')

api_id = 'b6prjz6zv3'

resources = client.get_resources(restApiId=api_id)
root_id = [resource for resource in resources["items"] if resource["path"] == "/"][0]["id"]



report_resource = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='create_report'
)
report_resource_id = report_resource["id"]



report_method = client.put_method(
    restApiId=api_id,
    resourceId=report_resource_id,
    httpMethod='POST',
    authorizationType='NONE'
)

report_response = client.put_method_response(
    restApiId=api_id,
    resourceId=report_resource_id,
    httpMethod='POST',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': False,
        'method.response.header.Access-Control-Allow-Origin': False,
        'method.response.header.Access-Control-Allow-Methods': False
    },
    responseModels={
        'application/json': 'Empty'
    }
)


report_integration = client.put_integration(
    restApiId=api_id,
    resourceId=report_resource_id,
    httpMethod='POST',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)


report_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=report_resource_id,
    httpMethod='POST',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': '\'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token\'',
        'method.response.header.Access-Control-Allow-Methods': '\'POST\'',
        'method.response.header.Access-Control-Allow-Origin': '\'*\''
    },
    # ithink they have an issue with real JSON here
    responseTemplates={
        "application/json": json.dumps({
            "msg_str": "report requested, check your phone shortly"
        })
    }
)


print ("DONE")

```
## Deploying the API
<h5>
From the top, choose Deploy API button and then fill in the details:.

Deployment stage:  *New Stage*.

Stage name: prod

Stage description: (leave blank)

Deployment description: (leave blank)

Choose Deploy
</h5>

## Update the API
```sh
import boto3
S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "c152200a3914245l9333592t1w655664160213-s3bucket-tliwtwia4yvv"

filename = "/home/ec2-user/environment/resources/website/config.js"
S3API.upload_file(filename, bucket_name, "config.js", ExtraArgs={'ContentType': "application/js", "CacheControl": "max-age=0"})


print ("DONE")
```