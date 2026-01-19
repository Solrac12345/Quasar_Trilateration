from fastapi import APIRouter, HTTPException
from app.models.request_models import TopSecretRequest
from app.services.location_service import get_location
from app.services.message_service import get_message

# Router for the /topsecret endpoint (EN)
# Routeur pour l'endpoint /topsecret (FR)
router = APIRouter(prefix="/topsecret", tags=["topsecret"])

@router.post("/")
def topsecret(req: TopSecretRequest):
    # Required satellite order for trilateration (EN)
    # Ordre requis des satellites pour la trilatération (FR)
    name_order = ["kenobi", "skywalker", "sato"]

    # Map satellites by name for quick access (EN)
    # Associer les satellites par nom pour un accès rapide (FR)
    sat_map = {s.name.lower(): s for s in req.satellites}

    distances: list[float] = []
    messages: list[list[str]] = []

    try:
        # Extract distances and messages in the correct order (EN)
        # Extraire les distances et messages dans l'ordre correct (FR)
        for name in name_order:
            sat = sat_map[name]
            distances.append(sat.distance)
            messages.append(sat.message)
    except KeyError:
        # Missing one or more required satellites (EN)
        # Un ou plusieurs satellites requis sont manquants (FR)
        raise HTTPException(status_code=400, detail="Missing required satellites")

    # Compute emitter position from distances (EN)
    # Calculer la position de l'émetteur à partir des distances (FR)
    x, y = get_location(*distances)
    if x is None or y is None:
        raise HTTPException(status_code=404, detail="Position cannot be determined")

    # Reconstruct the original message (EN)
    # Reconstruire le message original (FR)
    msg = get_message(messages)
    if not msg:
        raise HTTPException(status_code=404, detail="Message cannot be determined")

    # Return structured response with position and message (EN)
    # Retourner une réponse structurée avec position et message (FR)
    return {
        "position": {"x": x, "y": y},
        "message": msg,
    }