# Spotlist

Este es un API para gestión musical construido con FastAPI y SQLModel.

## Características

- **CRUD Completo**: Usuarios, Artistas, Álbumes y Canciones.
- **Relaciones**:
  - Artista -> Álbumes (Uno a Muchos)
  - Álbum -> Canciones (Uno a Muchos)
  - Usuario <-> Artistas (Muchos a Muchos - Favoritos)
  - Usuario <-> Canciones (Muchos a Muchos - Favoritos)
- **Base de Datos**: SQLModel
- **Autenticación**: Supabase Auth
- **Almacenamiento**: Cloudinary

## Requisitos

- Python 3.11+

## Instalación

1.  **Clonar el repositorio**
2.  **Crear un entorno virtual**:
    ```
    python -m venv venv
    ```
3.  **Activar el entorno virtual**:
    - Windows: `.\venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
4.  **Instalar dependencias**:
    ```
    pip install -r requirements.txt
    ```

## Ejecución

Para iniciar el servidor de desarrollo:

```
uvicorn app.main:app --reload
```
La API estará disponible en `http://127.0.0.1:8000`.
El API de documentación estará en `http://127.0.0.1:8000/docs`.
En render con `https://spotlist-6xna.onrender.com/songs/`.

```
## 📚 Tabla de Contenidos
- [✨ Características](#-características)
- [🛠️ Tecnologías](#-tecnologías)
- [🏗️ Arquitectura](#-arquitectura)
- [📊 Modelos de Datos](#-modelos-de-datos)
- [🔌 Endpoints API](#-endpoints-api)
- [📦 Instalación](#-instalación)
- [⚙️ Configuración](#-configuración)
- [🚀 Uso](#-uso)
- [🌐 Despliegue](#-despliegue)
- [📝 Estructura de Datos](#-estructura-de-datos)
- [👨‍💻 Desarrollado por](#-desarrollado-por)
- [📄 Licencia](#-licencia)

---

## ✨ Características

- ✅ CRUD Completo para **Usuarios**, **Artistas**, **Álbumes** y **Canciones**
- ⭐ Sistema de **Favoritos** (Usuarios ↔ Artistas / Usuarios ↔ Canciones)
- 📤 Carga de imágenes con **Cloudinary**
- 🖥️ Interfaz web con **HTML + Jinja2**
- 🚀 API REST documentada automáticamente
- 🗄️ Base de datos relacional con **SQLModel**

---

## 🛠️ Tecnologías

### 🔧 Backend
- FastAPI  
- SQLModel  
- SQLite  
- Uvicorn  

### 🎨 Frontend
- Jinja2  
- HTML / CSS  

### ☁️ Servicios externos
- Cloudinary  

---

## 🏗️ Arquitectura

```bash
Spotlist/
├── app/
│   ├── main.py              # Entrada principal
│   ├── config.py            # Config vars
│   ├── database.py          # Conexión DB
│   ├── models.py            # Modelos SQLModel
│   ├── utils.py             # Utilidades (Cloudinary)
│   ├── routers/
│   │   ├── users.py         # CRUD Usuarios + Favoritos
│   │   ├── artists.py       # CRUD Artistas
│   │   ├── albums.py        # CRUD Álbumes
│   │   ├── songs.py         # CRUD Canciones
│   │   └── storage.py       # Storage
│   ├── services/
│   │   └── storage.py       # Lógica Cloudinary
│   ├── templates/           # HTML
│   └── static/              # CSS / JS
├── .env
├── requirements.txt
├── run.py
└── database.db
📊 Modelos de Datos
🔗 Diagrama de Relaciones
mermaid
Copiar código
erDiagram
    User ||--o{ UserArtistLink : "tiene"
    Artist ||--o{ UserArtistLink : "es favorito de"
    User ||--o{ UserSongLink : "tiene"
    Song ||--o{ UserSongLink : "es favorito de"
    Artist ||--o{ Album : "crea"
    Album ||--o{ Song : "contiene"

    User {
        int id PK
        string username
        string email
        string image_url
    }
    
    Artist {
        int id PK
        string name
        string genre
        string image_url
    }
    
    Album {
        int id PK
        string name
        int year
        int artist_id FK
        string image_url
    }
    
    Song {
        int id PK
        string name
        int duration
        int album_id FK
    }
    
    UserArtistLink {
        int user_id FK
        int artist_id FK
    }
    
    UserSongLink {
        int user_id FK
        int song_id FK
    }
🔌 Endpoints API
👤 Usuarios
Método	Endpoint	Descripción
GET	/users/	Listar usuarios
GET	/users/{id}	Obtener usuario
GET	/users/create	Formulario
POST	/users/create	Crear usuario
POST	/users/{id}/delete	Eliminar usuario

⭐ Favoritos
Método	Endpoint	Descripción
POST	/users/{id}/favorites/{artist_id}	Agregar artista
POST	/users/{id}/favorites/{artist_id}/delete	Quitar artista
POST	/users/{id}/favorites/songs/{song_id}	Agregar canción
POST	/users/{id}/favorites/songs/{song_id}/delete	Quitar canción

🎤 Artistas
Método	Endpoint	Descripción
GET	/artists/	Listar artistas
GET	/artists/{id}	Obtener artista
GET	/artists/create	Formulario
POST	/artists/create	Crear artista
POST	/artists/{id}/delete	Eliminar artista

💿 Álbumes
Método	Endpoint	Descripción
GET	/albums/	Listar álbumes
GET	/albums/{id}	Obtener álbum
GET	/albums/create	Formulario
POST	/albums/create	Crear álbum
POST	/albums/{id}/delete	Eliminar álbum

🎵 Canciones
Método	Endpoint	Descripción
GET	/songs/	Listar canciones
GET	/songs/{id}	Obtener canción
GET	/songs/create	Formulario
POST	/songs/create	Crear canción
POST	/songs/{id}/delete	Eliminar canción

📦 Instalación
1️⃣ Clonar
bash
Copiar código
git clone <repo-url>
cd Spotlist
2️⃣ Crear entorno
bash
Copiar código
python -m venv venv
3️⃣ Activar
Windows:

bash
Copiar código
.\venv\Scripts\activate
Linux/Mac:

bash
Copiar código
source venv/bin/activate
4️⃣ Instalar dependencias
bash
Copiar código
pip install -r requirements.txt
⚙️ Configuración
Crear archivo .env:

env
Copiar código
database_url="sqlite:///./database.db"

cloudinary_cloud_name="your_cloud"
cloudinary_api_key="your_key"
cloudinary_api_secret="your_secret"
🚀 Uso
Iniciar servidor
bash
Copiar código
uvicorn app.main:app --reload
Accesos
🌐 Web: http://localhost:8000

📘 API Docs: http://localhost:8000/docs

🔵 Redoc: http://localhost:8000/redoc

🌐 Despliegue en Render
Build Command:

bash
Copiar código
pip install -r requirements.txt
Start Command:

bash
Copiar código
uvicorn app.main:app --host 0.0.0.0 --port $PORT
📝 Estructura de Datos
Usuario
json
Copiar código
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "image_url": "https://cloudinary.com/...",
  "favorite_artists": [],
  "favorite_songs": []
}
Artista
json
Copiar código
{
  "id": 1,
  "name": "The Beatles",
  "genre": "Rock",
  "image_url": "https://cloudinary.com/...",
  "albums": []
}
Álbum
json
Copiar código
{
  "id": 1,
  "name": "Abbey Road",
  "year": 1969,
  "artist_id": 1,
  "image_url": "https://cloudinary.com/...",
  "songs": []
}
Canción
json
Copiar código
{
  "id": 1,
  "name": "Come Together",
  "duration": 259,
  "album_id": 1
}
 Desarrollado por
Daniel Felipe Gomez Cordoba
GitHub: @DanielGomezC04
