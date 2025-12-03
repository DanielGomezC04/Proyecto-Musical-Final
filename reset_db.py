import os
from sqlmodel import SQLModel
from app.database import engine
from app.models import * # Importar todos los modelos para que SQLModel los reconozca

def reset_database():
    print("🗑️  Eliminando base de datos antigua...")
    try:
        if os.path.exists("database.db"):
            os.remove("database.db")
            print("✅ Archivo database.db eliminado.")
        else:
            print("ℹ️  No existía database.db.")
    except PermissionError:
        print("❌ Error: No se pudo borrar el archivo. Asegúrate de detener el servidor (Ctrl+C) antes de ejecutar esto.")
        return

    print("✨ Creando nuevas tablas...")
    SQLModel.metadata.create_all(engine)
    print("✅ Base de datos recreada exitosamente con la nueva estructura (artist_name).")

if __name__ == "__main__":
    reset_database()
