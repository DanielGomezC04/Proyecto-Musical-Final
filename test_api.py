import requests

# URL base de la API
BASE_URL = "http://127.0.0.1:8000"

def test_create_song():
    print("Probando creación de canción...")
    
    # Datos de la canción (JSON válido)
    song_data = {
        "title": "Bohemian Rhapsody",
        "artist_name": "Queen"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/songs/", json=song_data)
        
        if response.status_code == 200:
            print("✅ Éxito! Canción creada:")
            print(response.json())
        else:
            print(f"❌ Error {response.status_code}:")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ No se pudo conectar al servidor. Asegúrate de que esté corriendo (uvicorn app.main:app --reload)")

if __name__ == "__main__":
    test_create_song()
