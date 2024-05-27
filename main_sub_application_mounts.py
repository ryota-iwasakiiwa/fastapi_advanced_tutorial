from fastapi import FastAPI

app = FastAPI()

@app.get("/app")
def read_main():
    return {"message": "Hello World from the main application"}


subapi = FastAPI()

@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from the sub application"}

app.mount("/subapi", subapi)