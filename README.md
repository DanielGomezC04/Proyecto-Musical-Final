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
## Desarrollado por:

- [Daniel Felipe Gomez Cordoba](https://github.com/DanielGomezC04)

##  Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Arquitectura](#-arquitectura)
- [Modelos de Datos](#-modelos-de-datos)
- [Endpoints API](#-endpoints-api)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Despliegue](#-despliegue)

##  Características

-  **CRUD Completo** para Usuarios, Artistas, Álbumes y Canciones
-  **Sistema de Favoritos** (Usuarios ↔ Artistas, Usuarios ↔ Canciones)
-  **Carga de Imágenes** con Cloudinary
-  **Interfaz Web** con templates HTML
-  **API REST** documentada automáticamente
-  **Base de datos relacional** con Cloudinary

##  Tecnologías

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

##  Arquitectura

```
Spotlist/
├── app/
│   ├── __init__.py
│   ├── main.py              # Punto de entrada de la aplicación
│   ├── config.py            # Configuración y variables de entorno
│   ├── database.py          # Configuración de base de datos
│   ├── models.py            # Modelos SQLModel
│   ├── utils.py             # Utilidades (upload de imágenes)
│   ├── routers/             # Endpoints API
│   │   ├── users.py         # CRUD Usuarios + Favoritos
│   │   ├── artists.py       # CRUD Artistas
│   │   ├── albums.py        # CRUD Álbumes
│   │   ├── songs.py         # CRUD Canciones
│   │   └── storage.py       # Gestión de archivos
│   ├── services/            # Lógica de negocio
│   │   └── storage.py       # Servicio de Cloudinary
│   ├── templates/           # Templates HTML
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── users/
│   │   ├── artists/
│   │   ├── albums/
│   │   └── songs/
│   └── static/              # Archivos estáticos (CSS, JS)
├── .env                     # Variables de entorno
├── requirements.txt         # Dependencias Python
├── run.py                   # Script de ejecución
└── database.db             # Base de datos SQLite
```

## 📊 Modelos de Datos

### Diagrama de Relaciones

```
    User ||--o{ UserArtistLink : "tiene"
    Artist ||--o{ UserArtistLink : "es favorito de"
    User ||--o{ UserSongLink : "tiene"
    Song ||--o{ UserSongLink : "es favorito de"
    Artist ||--o{ Album : "crea"
    Album ||--o{ Song : "contiene"
```

### Relaciones

1. **Artist → Albums** (Uno a Muchos)
   - Un artista puede tener múltiples álbumes
   
2. **Album → Songs** (Uno a Muchos)
   - Un álbum puede tener múltiples canciones

3. **User ↔ Artists** (Muchos a Muchos - Favoritos)
   - Un usuario puede tener múltiples artistas favoritos
   - Un artista puede ser favorito de múltiples usuarios
   - Tabla intermedia: `UserArtistLink`

4. **User ↔ Songs** (Muchos a Muchos - Favoritos)
   - Un usuario puede tener múltiples canciones favoritas
   - Una canción puede ser favorita de múltiples usuarios
   - Tabla intermedia: `UserSongLink`

## 🔌 Endpoints API

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

## 📦 Instalación

### Requisitos Previos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd Spotlist
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuración

### Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
# Base de datos
database_url="sqlite:///./database.db"

# Cloudinary (para imágenes)
cloudinary_cloud_name="tu_cloud_name"
cloudinary_api_key="tu_api_key"
cloudinary_api_secret="tu_api_secret"
```

### Obtener Credenciales de Cloudinary

1. Crear cuenta en [Cloudinary](https://cloudinary.com/)
2. Ir al Dashboard
3. Copiar: Cloud Name, API Key, API Secret
4. Pegar en el archivo `.env`

## 🚀 Uso

### Desarrollo Local

1. **Iniciar el servidor**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Acceder a la aplicación**
   - Interfaz web: `http://127.0.0.1:8000`
   - Documentación API: `http://127.0.0.1:8000/docs`
   - Documentación alternativa: `http://127.0.0.1:8000/redoc`

### Flujo de Uso

1. **Crear Artistas** → `/artists/create`
2. **Crear Álbumes** → `/albums/create` (seleccionar artista)
3. **Crear Canciones** → `/songs/create` (seleccionar álbum)
4. **Crear Usuarios** → `/users/create`
5. **Agregar Favoritos** → Ir a un usuario → Seleccionar artista/canción → Agregar

## 🌐 Despliegue

### Render

1. **Crear cuenta en [Render](https://render.com/)**

2. **Crear nuevo Web Service**
   - Conectar repositorio de GitHub
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

3. **Configurar Variables de Entorno**
   - Agregar las mismas variables del archivo `.env`

4. **Desplegar**
   - Render automáticamente desplegará la aplicación

### Consideraciones de Producción

- **Base de datos**: Considerar migrar a PostgreSQL para producción
- **Imágenes**: Cloudinary maneja el almacenamiento en la nube
- **HTTPS**: Render proporciona certificados SSL automáticos

## 📝 Estructura de Datos

### Usuario
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "image_url": "https://cloudinary.com/...",
  "favorite_artists": [...],
  "favorite_songs": [...]
}
```

### Artista
```json
{
  "id": 1,
  "name": "The Beatles",
  "genre": "Rock",
  "image_url": "https://cloudinary.com/...",
  "albums": [...]
}
```

### Álbum
```json
{
  "id": 1,
  "name": "Abbey Road",
  "year": 1969,
  "artist_id": 1,
  "image_url": "https://cloudinary.com/...",
  "songs": [...]
}
```

### Canción
```json
{
  "id": 1,
  "name": "Come Together",
  "duration": 259,
  "album_id": 1
}
```

## 👨‍💻 Desarrollado por

**Daniel Felipe Gomez Cordoba**
- GitHub: [@DanielGomezC04](https://github.com/DanielGomezC04)

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

**Nota**: Este proyecto fue desarrollado como parte de un ejercicio académico/profesional de desarrollo web con FastAPI.

