from typing import Dict
from app.models.request_models import SatelliteData

# Simple in-memory store for satellite data in split mode (EN)
# Stockage simple en mémoire pour les données satellites en mode fragmenté (FR)
satellite_data: Dict[str, SatelliteData] = {}