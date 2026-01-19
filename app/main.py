from fastapi import FastAPI
from app.config import settings
from app.routers import topsecret, topsecret_split

# Initialize FastAPI using configuration values (EN)
# Initialiser FastAPI en utilisant les valeurs de configuration (FR)
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Register routers/endpoints (EN)
# Enregistrer les routeurs/endpoints (FR)
app.include_router(topsecret.router)
app.include_router(topsecret_split.router)

