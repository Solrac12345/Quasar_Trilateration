import uvicorn
from app.config import settings

# Return and close use in you terminal "uvicorn app.main:app --reload" will avoid frozen terminal
# Pour éviter un terminal gelé, utilisez dans votre terminal "uvicorn app.main:app --reload"
# Start the FastAPI application using configuration values (EN)
# Démarrer l'application FastAPI en utilisant les valeurs de configuration (FR)
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.API_PORT,
        reload=True  # Auto-reload in development (EN) / Rechargement auto en développement (FR)
    )