import uvicorn
from database import engine

import models
from fastapi import FastAPI
from router import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)