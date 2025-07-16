import os
import glob

confirm = input("⚠️  Are you sure you want to DELETE the database and ALL migration files? (y/N): ").strip().lower()

if confirm != "y":
    print("Aborted.")
    exit(0)

# Delete db.sqlite3
if os.path.exists("db.sqlite3"):
    os.remove("db.sqlite3")
    print("🗑️ Deleted db.sqlite3")

# Delete all migration files except __init__.py
for root, dirs, files in os.walk("."):
    if "migrations" in dirs:
        migration_path = os.path.join(root, "migrations")
        for file in glob.glob(os.path.join(migration_path, "*.py")):
            if not file.endswith("__init__.py"):
                os.remove(file)
                print(f"🗑️ Deleted {file}")
        for file in glob.glob(os.path.join(migration_path, "*.pyc")):
            os.remove(file)
            print(f"🗑️ Deleted {file}")

print("✔️ Reset complete. Run makemigrations and migrate next.")
