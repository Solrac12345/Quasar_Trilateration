print(">>> USING NEW LOCATION SERVICE <<<")

import numpy as np

# Satellite coordinates (EN)
# Coordonnées des satellites (FR)
SATELLITES = {
    "kenobi": np.array([-500.0, -200.0]),
    "skywalker": np.array([100.0, -100.0]),
    "sato": np.array([500.0, 100.0]),
}

def get_location(d1: float, d2: float, d3: float):
    
    # Extract satellite positions (EN)
    # Extraire les positions des satellites (FR)
    P1 = SATELLITES["kenobi"]
    P2 = SATELLITES["skywalker"]
    P3 = SATELLITES["sato"]

    # Vector from P1 to P2 (EN)
    # Vecteur de P1 à P2 (FR)
    ex = (P2 - P1)
    d = np.linalg.norm(ex)
    ex = ex / d

    # Vector from P1 to P3 (EN)
    # Vecteur de P1 à P3 (FR)
    P3P1 = P3 - P1
    i = np.dot(ex, P3P1)

    # Orthogonal vector (EN)
    # Vecteur orthogonal (FR)
    ey = (P3P1 - i * ex)
    ey = ey / np.linalg.norm(ey)

    # Coordinates in the new basis (EN)
    # Coordonnées dans la nouvelle base (FR)
    j = np.dot(ey, P3P1)

    # Compute x coordinate (EN)
    # Calculer la coordonnée x (FR)
    x = (d1**2 - d2**2 + d**2) / (2 * d)

    # Compute y coordinate (EN)
    # Calculer la coordonnée y (FR)
    y = (d1**2 - d3**2 + i**2 + j**2 - 2 * i * x) / (2 * j)

    # Convert back to global coordinates (EN)
    # Convertir en coordonnées globales (FR)
    final_pos = P1 + x * ex + y * ey

    return float(final_pos[0]), float(final_pos[1])