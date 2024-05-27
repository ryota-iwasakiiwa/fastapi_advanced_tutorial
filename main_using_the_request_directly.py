from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}