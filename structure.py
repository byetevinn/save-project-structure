import os
import json

# ===========================================
# Este script gera um arquivo JSON contendo
# a estrutura de diretórios de um projeto.
# Ele ignora arquivos e/ou pastas conforme
# duas listas de controle:
# - IGNORE_ALL: ignora arquivos/pastas por completo
# - IGNORE_FILES_IN: ignora apenas arquivos dentro de pastas específicas,
#                    mas permite que suas subpastas apareçam
# ===========================================

# Lista de nomes a serem completamente ignorados (arquivos ou pastas)
IGNORE_ALL = [
    "venv",
    "__pycache__",
    ".git",
    ".env",
    "README.md",
    "structure.py",
]

# Lista de pastas onde os arquivos devem ser ignorados (mas subpastas são permitidas)
IGNORE_FILES_IN = [
    "screenshots",
    "processed",
    "sites",
]


def build_structure(path, root_path):
    """Cria recursivamente a estrutura de diretórios, ignorando conforme regras globais"""
    relative_path = os.path.relpath(path, root_path)
    parts = relative_path.split(os.sep)

    # Ignora se qualquer parte do caminho está em IGNORE_ALL
    if any(part in IGNORE_ALL for part in parts):
        return None

    name = os.path.basename(path)

    if os.path.isdir(path):
        children = []
        for item in sorted(os.listdir(path)):
            full_path = os.path.join(path, item)
            child_structure = build_structure(full_path, root_path)
            if child_structure:
                children.append(child_structure)
        return {"name": name, "type": "folder", "children": children}
    else:
        # Ignora arquivos dentro de pastas em IGNORE_FILES_IN
        if any(part in IGNORE_FILES_IN for part in parts[:-1]):
            return None
        return {"name": name, "type": "file"}


# Obtém o caminho absoluto da pasta atual e o nome da raiz
root_path = os.path.abspath(".")
root_name = os.path.basename(root_path)

# Cria a estrutura a partir do diretório atual
structure = build_structure(root_path, root_path)

# Atualiza o nome da raiz com o nome real da pasta
if structure:
    structure["name"] = root_name

# Salva a estrutura gerada em um arquivo JSON
with open("project_structure.json", "w", encoding="utf-8") as f:
    json.dump(structure, f, indent=4, ensure_ascii=False)
