import json

with open('/Users/easy/programming/wp-3rd/app/static/json/info.json') as Json: doc = json.loads(Json.read())
DB_HOST = doc["sqlHOST"]
DB_USER = doc["sqlID"]
DB_PASSWORD = doc["sqlPW"]
DB_NAME = doc["sqlTABLE"]

def DatabaseConfig():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
