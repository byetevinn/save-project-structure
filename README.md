# Estrutura de Diretórios - Gerador JSON

Este projeto tem como objetivo **gerar automaticamente um arquivo JSON** contendo a estrutura de diretórios de um projeto, de forma organizada e personalizável.

## 📁 O que o script faz?

O script `main.py` percorre recursivamente os diretórios e subdiretórios a partir do local onde ele é executado, e gera um arquivo chamado `project_structure.json` com a hierarquia completa dos arquivos e pastas, ignorando elementos definidos por regras específicas.

---

## ⚙️ Regras de Ignoração

Existem duas listas de controle para ignorar arquivos/pastas:

- **IGNORE_ALL**: ignora arquivos e pastas completamente (ex: `venv`, `.git`, `README.md`).
- **IGNORE_FILES_IN**: ignora **apenas arquivos** dentro de certas pastas (mas permite mostrar suas subpastas).

---

## 📄 Exemplo de saída

Um arquivo `project_structure.json` será gerado com a seguinte estrutura:

```json
{
    "name": "nome_da_pasta_raiz",
    "type": "folder",
    "children": [
        {
            "name": "src",
            "type": "folder",
            "children": [
                {
                    "name": "main.py",
                    "type": "file"
                }
            ]
        },
        ...
    ]
}
```

---

## 🚀 Como usar

1. Clone o repositório ou copie os arquivos para o seu projeto.
2. Execute o script:

```bash
python main.py
```

3. O arquivo `project_structure.json` será criado com a estrutura do projeto.

---

## 📦 Arquivos do Projeto

- `.gitignore`: configurações de arquivos/pastas a serem ignorados pelo Git.
- `main.py`: script principal para gerar a estrutura JSON.
- `README.md`: este arquivo de documentação.

---

## 🧠 Requisitos

- Python 3.6+

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para utilizar e modificar conforme necessário.

---
