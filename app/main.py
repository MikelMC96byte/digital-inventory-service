from fastapi import FastAPI
from routers import companies, company_groups
from private import traces
import uvicorn

app = FastAPI()

# public routes
app.include_router(companies.router)
app.include_router(company_groups.router)
# private routes
app.include_router(prefix="/admin", router=traces.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/ping")
async def ping():
    return {"message": "Hi!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")