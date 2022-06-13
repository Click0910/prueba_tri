from fastapi import FastAPI
from routes.routes import routes

app = FastAPI(
    title='Prueba Tri'
)

app.include_router(routes)
