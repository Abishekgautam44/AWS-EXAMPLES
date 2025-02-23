## DynamoDB AWS CLI and SDK Operations

# Listing DyanamoDB Tables
```sh
aws dynamodb list-tables --region us-east-1
```
# Batch Operations
```sh

import boto3, json


def batch_put(food_list):
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('FoodProducts')
    #with table.batch_writer(overwrite_by_pkeys=['product_name']) as batch: ##overwrites
    with table.batch_writer() as batch:   #doesn't allow duplications batch fails
        for food in food_list:
            product_name = food['product_name_str']
            price_in_cents = food['price_in_cents_int']
            formatted_item = {
                'product_name': product_name,
                'price_in_cents': price_in_cents  #Boto will "know" this is a number type
            }
            print("Adding food item:", formatted_item)
            batch.put_item(Item=formatted_item)

   
if __name__ == '__main__':
    with open("../resources/test.json") as json_file:
        food_list = json.load(json_file)
    batch_put(food_list)

```
## Querying the table by using the SDK
# Get all Items
```sh
import boto3


def get_all_items():
    import boto3

    DDB = boto3.resource('dynamodb', region_name='us-east-1')

    table = DDB.Table('FoodProducts')

    response = table.scan()
    data = response['Items']
    
    while response.get('LastEvaluatedKey'):
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    print (data)
    
if __name__ == '__main__':
    get_all_items()

```
# Get Single Items
```sh
import boto3, json
from boto3.dynamodb.conditions import Key


def get_one_item(product):

    DDB = boto3.client('dynamodb', region_name='us-east-1')

    response = DDB.get_item(TableName='FoodProducts',
        Key={
         'product_name': {'S': product}
         }
        )

    data = response['Item']
    
    print (data)
 
if __name__ == '__main__':
    product = "chocolate cake"
    get_one_item(product)

```
## Adding a global secondary index to the table
```sh
import boto3
from boto3.dynamodb.conditions import Key

def update_table():

    DDB = boto3.client('dynamodb', region_name='us-east-1')

    params = {
        'TableName': 'FoodProducts',
        'AttributeDefinitions': [
            {'AttributeName': 'special', 'AttributeType': 'N'}
        ],
        'GlobalSecondaryIndexUpdates': [
            {
                'Create': {
                    'IndexName': 'special_GSI',
                    'KeySchema': [
                        {
                            'AttributeName': 'special',
                            'KeyType': 'HASH'
                        }
                    ],
                        'Projection': {
                        'ProjectionType': 'ALL'
                    },
                        'ProvisionedThroughput': {
                        'ReadCapacityUnits': 1,
                        'WriteCapacityUnits': 1
                    }
                }
            }
        ]
    }

    table = DDB.update_table(**params)
    print ('Done')
    

if __name__ == '__main__':
    update_table()
```
## Filtering the query form GSI With tags
```sh

import boto3, json
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Key, Attr, Not


def scan_menu_items():
    
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('FoodProducts')

    response = table.scan(
                IndexName='special_GSI',
                FilterExpression=Not(Attr('tags').contains('out of stock')))
        
    data = response['Items']
    
    print (data)
 
if __name__ == '__main__':
    scan_menu_items()
```
