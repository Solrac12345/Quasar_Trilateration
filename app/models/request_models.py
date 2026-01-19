from typing import List
from pydantic import BaseModel

# Data model for a satellite in /topsecret (EN)
# Modèle de données pour un satellite dans /topsecret (FR)
class Satellite(BaseModel):
    name: str
    distance: float
    message: List[str]

# Request body model for /topsecret (EN)
# Modèle du corps de requête pour /topsecret (FR)
class TopSecretRequest(BaseModel):
    satellites: List[Satellite]

# Data model for a single satellite in /topsecret_split (EN)
# Modèle de données pour un satellite dans /topsecret_split (FR)
class SatelliteData(BaseModel):
    distance: float
    message: List[str]