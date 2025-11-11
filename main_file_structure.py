import os
import sys

# Use this structure: top-level dict where each key is a folder name (use "." for repo root)
structure = {
    ".": [".env", ".env-example", ".gitignore", "README.md", "requirements.txt"],
    "src": [
        "alembic.ini",
        "main.py",
        "__init__.py",
        {
            "api": [
                "__init__.py",
                {"routers": ["__init__.py"]},
                {"v1": ["__init__.py"]},
            ],
            "app": [
                "__init__.py",
                "config.py",
                {"middleware": ["__init__.py"]},
            ],
            "core": [
                "__init__.py",
                "db.py",
                "logger.py",
                {"common": ["__init__.py", "exceptions.py"]},
                {"dependencies": ["__init__.py", "pagination.py"]},
            ],
            "migrations": [
                "env.py",
                "README.md",
                "script.py.mako",
                {"versions": []},
            ],
            "models": [
                "__init__.py",
                "base.py",
                {
                    "schemas": [
                        "__init__.py",
                        "base.py",
                        {"common": ["__init__.py", "response.py"]},
                    ]
                },
            ],
            "services": ["__init__.py"],
            "tests": ["__init__.py"],
            "utils": ["__init__.py"],
        },
    ],
}


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def create_from_list(base_path: str, items: list):
    """
    items: list where each element is either:
      - str -> create file at base_path/str
      - dict -> { folder_name: [ ...contents... ] }
    """
    for item in items:
        if isinstance(item, str):
            target = os.path.join(base_path, item)
            # If item looks like a filename, create file. If it has no extension but user still wants file, create it.
            if not os.path.exists(target):
                # Ensure parent dir exists (should)
                parent = os.path.dirname(target)
                if parent and not os.path.exists(parent):
                    os.makedirs(parent, exist_ok=True)
                open(target, "w", encoding="utf-8").close()
        elif isinstance(item, dict):
            for folder_name, contents in item.items():
                folder_path = os.path.join(base_path, folder_name)
                ensure_dir(folder_path)
                # contents should be a list
                if isinstance(contents, list):
                    create_from_list(folder_path, contents)
                else:
                    # if contents is empty or not list, just ensure folder
                    continue
        else:
            # ignore unknown types
            continue


def create_structure(root: str, tree: dict):
    """
    tree: dict mapping folder -> list(contents).
    Use '.' as key for files/folders at repository root.
    """
    for folder, contents in tree.items():
        # Compute path for this folder
        folder_path = os.path.join(root, folder) if folder not in (".", "") else root
        ensure_dir(folder_path)
        if isinstance(contents, list):
            create_from_list(folder_path, contents)
        else:
            # if contents is a dict directly, handle that
            if isinstance(contents, dict):
                for k, v in contents.items():
                    sub_path = os.path.join(folder_path, k)
                    ensure_dir(sub_path)
                    if isinstance(v, list):
                        create_from_list(sub_path, v)


if __name__ == "__main__":
    base_dir = os.getcwd()
    print(f"🚀 Creating FastAPI project structure in: {base_dir}")
    try:
        create_structure(base_dir, structure)
        print("✅ Folder structure created successfully!")
    except Exception as e:
        print("❌ Error creating structure:", e)
        sys.exit(1)
