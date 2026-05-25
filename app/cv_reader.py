from pathlib import Path


def read_text_file(path: str) -> str:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"No existe el archivo: {path}")

    return file_path.read_text(encoding="utf-8")