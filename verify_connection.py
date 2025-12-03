import asyncio
from app.database import engine
from app.services.storage import supabase
from sqlmodel import text, Session

def check_db():
    print("Checking Database Connection...")
    try:
        with Session(engine) as session:
            result = session.exec(text("SELECT 1")).first()
            print(f"Database Connection Successful! Result: {result}")
    except Exception as e:
        print(f"Database Connection FAILED: {e}")

def check_storage():
    print("\nChecking Storage Configuration...")
    try:
        print("Supabase Client Initialized.")
        print("Ensure you have created the following buckets in your Supabase project:")
        print("- artist-images")
        print("- profile-images")
        print("- album-covers")
        print("(Note: This script cannot verify if buckets exist without making a request that might fail if empty)")
        
    except Exception as e:
        print(f"Storage Check FAILED: {e}")

if __name__ == "__main__":
    check_db()
    check_storage()
