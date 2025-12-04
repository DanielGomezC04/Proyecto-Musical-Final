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

## Tecnologías

### Backend
- **FastAPI** - Framework web moderno y rápido
- **SQLModel** - ORM basado en Pydantic y SQLAlchemy
- **SQLite** - Base de datos (desarrollo)
- **Uvicorn** - Servidor ASGI

### Frontend
- **Jinja2** - Motor de templates
- **HTML/CSS** - Interfaz de usuario

### Servicios Externos
- **Cloudinary** - Almacenamiento de imágenes

## Modelos de Datos

### Diagrama de Relaciones

```
```

## Endpoints API

### Usuarios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/users/` | Lista todos los usuarios |
| `GET` | `/users/{user_id}` | Obtiene un usuario específico |
| `GET` | `/users/create` | Formulario de creación |
| `POST` | `/users/create` | Crea un nuevo usuario |
| `POST` | `/users/{user_id}/delete` | Elimina un usuario |

### Favoritos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/users/{user_id}/favorites/{artist_id}` | Agrega artista a favoritos |
| `POST` | `/users/{user_id}/favorites/{artist_id}/delete` | Elimina artista de favoritos |
| `POST` | `/users/{user_id}/favorites/songs/{song_id}` | Agrega canción a favoritos |
| `POST` | `/users/{user_id}/favorites/songs/{song_id}/delete` | Elimina canción de favoritos |

### Artistas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/artists/` | Lista todos los artistas |
| `GET` | `/artists/{artist_id}` | Obtiene un artista específico |
| `GET` | `/artists/create` | Formulario de creación |
| `POST` | `/artists/create` | Crea un nuevo artista |
| `POST` | `/artists/{artist_id}/delete` | Elimina un artista |

### Álbumes

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/albums/` | Lista todos los álbumes |
| `GET` | `/albums/{album_id}` | Obtiene un álbum específico |
| `GET` | `/albums/create` | Formulario de creación |
| `POST` | `/albums/create` | Crea un nuevo álbum |
| `POST` | `/albums/{album_id}/delete` | Elimina un álbum |

### Canciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/songs/` | Lista todas las canciones |
| `GET` | `/songs/{song_id}` | Obtiene una canción específica |
| `GET` | `/songs/create` | Formulario de creación |
| `POST` | `/songs/create` | Crea una nueva canción |
| `POST` | `/songs/{song_id}/delete` | Elimina una canción |

## Despliegue

### Render

1. **Crear cuenta en [Render](https://render.com/)**

2. **Crear nuevo Web Service**
   - Conectar repositorio de GitHub
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

3. **Desplegar**
   - Render automáticamente desplegará la aplicación

### Consideraciones de Producción

- **Base de datos**: SQLite para desarrollo, considerar PostgreSQL para producción
- **Imágenes**: Cloudinary maneja el almacenamiento en la nube
- **HTTPS**: Render proporciona certificados SSL automáticos

## Desarrollado por

**Daniel Felipe Gomez Cordoba**
- GitHub: [@DanielGomezC04](https://github.com/DanielGomezC04)

---
