import os
from dotenv import load_dotenv

# Load environment variables from the .env file (EN)
# Charger les variables d'environnement depuis le fichier .env (FR)
load_dotenv()

class Settings:
    # Read configuration values with sensible defaults (EN)
    # Lire les valeurs de configuration avec des valeurs par défaut raisonnables (FR)
    APP_ENV: str = os.getenv("APP_ENV", "development")
    APP_NAME: str = os.getenv("APP_NAME", "QuasarOperation")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    API_PORT: int = int(os.getenv("API_PORT", 8000))

# Single settings instance used across the app (EN)
# Instance unique de configuration utilisée dans toute l'application (FR)
settings = Settings()