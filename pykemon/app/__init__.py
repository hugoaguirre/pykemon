from fastapi import FastAPI

from pykemon.app.routers import pokemon

PREFIX = "/api/pykemon"

app = FastAPI(
    title="Pykemon v1",
    description="Wrapper for PokeAPI written in Python",
    openapi_url=f"{PREFIX}/openapi.json",
    docs_url=f"{PREFIX}/docs",
    redoc_url=f"{PREFIX}/redoc",
)

app.include_router(pokemon.router, prefix=PREFIX)

app.mount(app=app, path=PREFIX)


@app.get("/")
def hello():
    return {"message": "Hello there, welcome to Pykemon!"}
