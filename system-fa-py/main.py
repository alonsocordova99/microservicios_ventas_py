from fastapi import FastAPI
from src.api.v1.auth_route import router as auth_router
from src.api.v1.empresa_route import router as empresa_router
from src.api.v1.clientes_route import router as clientes_router
from src.api.v1.productos_route import router as productos_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static/files", StaticFiles(directory="static/files"), name="files")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(empresa_router)
app.include_router(clientes_router)
app.include_router(productos_router)

