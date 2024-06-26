from contextlib import asynccontextmanager

from fastapi import FastAPI

def fake_answer_to_everything_ml_model(x: float):
    return x * 42

ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    " Clean up the ML model and release the resources"
    ml_models.clear()

app = FastAPI(lifespan=lifespan)
# app = FastAPI()

items = {}

# @app.on_event("startup")
# async def startup_event():
#     items["foo"] = {"name": "Fighters"}
#     items["bar"] = {"name": "Tenders"}

# @app.on_event("shutdown")
# def shutdown_event():
#     with open("log.txt", mode="a") as log:
#         log.write("Application shutdown")

@app.get("/predict")
async def predict(x: float):
    result = ml_models["answer_to_everything"](x)
    return {"result": result}

