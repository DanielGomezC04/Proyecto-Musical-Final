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

## Git

Generar commits:

```
git init
git add .
git commit -m "Initial commit: FastAPI scaffold with SQLModel"
# git remote add origin <tu-repo-url>
# git push -u origin main
```
## Desarrollado por:

- [Daniel Felipe Gomez Cordoba](https://github.com/DanielGomezC04)
