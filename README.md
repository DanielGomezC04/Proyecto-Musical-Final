# Proyecto Musical Backend (FastAPI)

Este es un scaffold para un backend de gestión musical construido con FastAPI y SQLModel.

## Características

- **CRUD Completo**: Usuarios, Artistas, Álbumes y Canciones.
- **Relaciones**:
  - Artista -> Álbumes (Uno a Muchos)
  - Álbum -> Canciones (Uno a Muchos)
  - Usuario <-> Artistas (Muchos a Muchos - Favoritos)
- **Base de Datos**: SQLite por defecto (fácil configuración).

## Requisitos

- Python 3.7+

## Instalación

1.  **Clonar el repositorio** (si aplica) o descargar los archivos.
2.  **Crear un entorno virtual**:
    ```bash
    python -m venv venv
    ```
3.  **Activar el entorno virtual**:
    - Windows: `.\venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
4.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.
La documentación interactiva (Swagger UI) estará en `http://127.0.0.1:8000/docs`.

## Git

Pasos sugeridos para control de versiones:

```bash
git init
git add .
git commit -m "Initial commit: FastAPI scaffold with SQLModel"
# git remote add origin <tu-repo-url>
# git push -u origin main
```
