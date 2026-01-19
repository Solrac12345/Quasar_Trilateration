from fastapi import APIRouter, HTTPException
from app.models.request_models import SatelliteData
from app.storage.memory_store import satellite_data
from app.services.location_service import get_location
from app.services.message_service import get_message


# Router for the /topsecret_split endpoints (EN)
# Routeur pour les endpoints /topsecret_split (FR)
router = APIRouter(prefix="/topsecret_split", tags=["topsecret_split"])

@router.post("/{name}")
def save_satellite(name: str, data: SatelliteData):
    # Store satellite data in memory under its name (EN)
    # Stocker les données du satellite en mémoire sous son nom (FR)
    satellite_data[name.lower()] = data
    return {"status": "saved", "satellite": name.lower()}

@router.get("/")
def get_info():
    # Satellites required to compute position and message (EN)
    # Satellites requis pour calculer la position et le message (FR)
    required = ["kenobi", "skywalker", "sato"]

    # Ensure all required satellites have been received (EN)
    # Vérifier que tous les satellites requis ont été reçus (FR)
    if not all(name in satellite_data for name in required):
        raise HTTPException(status_code=404, detail="Not enough information")

    # Collect distances and messages in the correct order (EN)
    # Récupérer distances et messages dans le bon ordre (FR)
    distances = [satellite_data[name].distance for name in required]
    messages = [satellite_data[name].message for name in required]

    # Compute position using trilateration (EN)
    # Calculer la position en utilisant la trilatération (FR)
    x, y = get_location(*distances)
    if x is None or y is None:
        raise HTTPException(status_code=404, detail="Position cannot be determined")

    # Reconstruct the original message (EN)
    # Reconstruire le message original (FR)
    msg = get_message(messages)
    if not msg:
        raise HTTPException(status_code=404, detail="Message cannot be determined")

    return {
        "position": {"x": x, "y": y},
        "message": msg,
    }