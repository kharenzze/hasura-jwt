from fastapi import FastAPI
import logging
import httpx
import os
import jwt
import uvicorn

logger = logging.getLogger("main")

app = FastAPI()
KEY = os.environ.get('JWT_KEY')
ALGORITHM = 'HS256'
body = {
    "https://hasura.io/jwt/claims": {
        "x-hasura-default-role": "admin",
        "x-hasura-allowed-roles": ["admin"]
    }
}
ADMIN_JWT = jwt.encode(body, KEY, algorithm=ALGORITHM)
default_headers = {
    "Authorization": "Bearer "+ ADMIN_JWT.decode("utf-8")
}

client = httpx.AsyncClient(headers=default_headers)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/users")
async def read_users():
    query = '''
    query {
        user {
            id
            name
            email
        }
    }
    '''
    body = {
        "query": query
    }
    r = await client.post("http://graphql-engine:8080/v1/graphql/", json=body)
    data  = r.json()
    return data