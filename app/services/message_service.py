print(">>> USING NEW MESSAGE SERVICE <<<")
from typing import List

def get_message(messages: List[List[str]]) -> str:

    # Determine the maximum message length (EN)
    # Déterminer la longueur maximale des messages (FR)
    max_len = max(len(m) for m in messages)

    # Pad messages on the RIGHT to align them (EN)
    # Compléter les messages à DROITE pour les aligner (FR)
    normalized = [m + [""] * (max_len - len(m)) for m in messages]

    result = []

    for i in range(max_len):
        # Pick the first non-empty word at each index (EN)
        # Choisir le premier mot non vide à chaque index (FR)
        for msg in normalized:
            if msg[i].strip():
                result.append(msg[i])
                break

    # Join words into a final sentence (EN)
    # Assembler les mots en une phrase finale (FR)
    return " ".join(result)