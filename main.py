import requests

def dish_fetch(num: int):
    try:
        # Llamada a la API con el id correcto
        url = f"https://api-colombia.com/api/v1/TypicalDish/{num}"
        datos = requests.get(url).json()

        # La API devuelve un objeto con id, name, description, etc.
        return {
            "id": datos.get("id", num),
            "name": datos.get("name", "Plato desconocido"),
            "description": datos.get("description", "¡Delicioso plato colombiano!")[:100] + "..."
        }

    except Exception:
        # Fallback en caso de error
        return {
            "id": num,
            "name": "Plato colombiano",
            "description": "¡Delicioso plato colombiano!"
        }