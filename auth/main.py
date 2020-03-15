from fastapi import FastAPI
import logging
import httpx
import os

logger = logging.getLogger("main")

app = FastAPI()
client = httpx.AsyncClient()
jwt_key = os.environ.get('JWT_KEY')

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