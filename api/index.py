import json
from urllib.parse import parse_qs

# Load JSON data once globally for efficiency
with open('q-vercel-python.json', 'r') as f:
    data = json.load(f)

def handler(event, context):
    # Parse query parameters
    query = event.get('queryStringParameters') or {}
    
    # The 'name' parameter could be a list or single string
    # Vercel passes repeated parameters in event['multiValueQueryStringParameters']
    names = []
    if 'name' in event.get('multiValueQueryStringParameters', {}):
        names = event['multiValueQueryStringParameters']['name']
    elif 'name' in query:
        names = [query['name']]
    
    # Lookup marks for requested names
    marks = [data.get(name, None) for name in names]
    
    # Return JSON response with CORS headers
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"marks": marks})
    }
