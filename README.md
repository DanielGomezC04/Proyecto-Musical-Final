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

##  Características

-  CRUD Completo para **Usuarios**, **Artistas**, **Álbumes** y **Canciones**
-  Sistema de **Favoritos** (Usuarios ↔ Artistas / Usuarios ↔ Canciones)
-  Carga de imágenes con **Cloudinary**
-  Interfaz web con **HTML + Jinja2**
-  API REST documentada automáticamente
-  Base de datos relacional con **SQLModel**

---

##  Tecnologías

###  Backend
- FastAPI  
- SQLModel  
- SQLite  
- Uvicorn  

###  Frontend
- Jinja2  
- HTML / CSS  

###  Servicios externos
- Cloudinary  

---
Usuarios
Método	Endpoint	Descripción
GET	/users/	Listar usuarios
GET	/users/{id}	Obtener usuario
GET	/users/create	Formulario
POST	/users/create	Crear usuario
POST	/users/{id}/delete	Eliminar usuario

Método	Endpoint	Descripción
POST	/users/{id}/favorites/{artist_id}	Agregar artista
POST	/users/{id}/favorites/{artist_id}/delete	Quitar artista
POST	/users/{id}/favorites/songs/{song_id}	Agregar canción
POST	/users/{id}/favorites/songs/{song_id}/delete	Quitar canción

 Artistas
Método	Endpoint	Descripción
GET	/artists/	Listar artistas
GET	/artists/{id}	Obtener artista
GET	/artists/create	Formulario
POST	/artists/create	Crear artista
POST	/artists/{id}/delete	Eliminar artista

 Álbumes
Método	Endpoint	Descripción
GET	/albums/	Listar álbumes
GET	/albums/{id}	Obtener álbum
GET	/albums/create	Formulario
POST	/albums/create	Crear álbum
POST	/albums/{id}/delete	Eliminar álbum

 Canciones
Método	Endpoint	Descripción
GET	/songs/	Listar canciones
GET	/songs/{id}	Obtener canción
GET	/songs/create	Formulario
POST	/songs/create	Crear canción
POST	/songs/{id}/delete	Eliminar canción

 Instalación
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
 Configuración
Crear archivo .env:

env
Copiar código
database_url="sqlite:///./database.db"

cloudinary_cloud_name="your_cloud"
cloudinary_api_key="your_key"
cloudinary_api_secret="your_secret"
 Uso
Iniciar servidor
bash
Copiar código
uvicorn app.main:app --reload
Accesos
 Web: http://localhost:8000

 API Docs: http://localhost:8000/docs

 Redoc: http://localhost:8000/redoc

 Despliegue en Render
Build Command:

bash
Copiar código
pip install -r requirements.txt
Start Command:

bash
Copiar código
uvicorn app.main:app --host 0.0.0.0 --port $PORT

 Desarrollado por
Daniel Felipe Gomez Cordoba
GitHub: @DanielGomezC04
