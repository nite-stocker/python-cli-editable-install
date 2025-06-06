# Python CLI project setup with pip and `pyproject.toml`  

This guide walks through creating a minimal, standards-compliant Python CLI tool using `pip`, `pyproject.toml`, and VS Code. The project installs in editable mode (`pip install -e .`), allowing the CLI to run globally during development without needing to rebuild.

It follows modern Python packaging practices (PEPs 517, 518, 621, 660) and serves as a reusable scaffold for future CLI tools.

Based on the [Real Python YouTube tutorial](https://www.youtube.com/watch?v=v6tALyc4C10) and [Real Python packaging course](https://realpython.com/courses/packaging-with-pyproject-toml/).

## Why use this pattern

- Run your CLI from anywhere (`myscript`)
- Follow Python packaging standards (`pyproject.toml`, editable installs)
- Avoid rebuilds after changes
- Integrate easily with IDEs, CI, and deployment tools

Without it:
- You’ll need to run scripts manually (`python file.py`)
- Structure may not support packaging or distribution
- Tooling (e.g. Poetry, build, pip) may not detect your project

## Step-by-step setup in VS Code

### 1. Create a new project folder

1. Open VS Code
2. Go to **File > Open Folder...**
3. Create a folder named `myscript` (or a custom name)
4. Select and open it

### 2. Add project files

From the **Explorer sidebar**:

- macOS: ⌘+Shift+E
- Windows/Linux: Ctrl+Shift+E

Create:

- `pyproject.toml`
- `README.md` (optional but recommended)

To create a new file:

- macOS: ⌘+N, then **File > Save As**
- Windows/Linux: Ctrl+N, then **File > Save As**

Paste into `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "myscript"
version = "0.1.0"
description = "Short description of what this script does"
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[project.scripts]
myscript = "myscript.main:main"
```

#### What is `pyproject.toml`

It is the standard project config file used by pip, build, and modern Python tools. It replaces `setup.py`.

- `[build-system]`: tells pip/setuptools how to build the package.
- `[project]`: defines metadata, dependencies, and the CLI entry point.
- `[project.scripts]`: maps a shell command (`myscript`) to the function to run (`main()` in `src/myscript/main.py`)

### 3. Create source files

From the Explorer:

- Create a folder: `src/`
- Inside `src/`, create another folder: `myscript/`
- Inside `src/myscript/`, create:
  - `__init__.py`
  - `main.py`

To create each file:

- macOS: ⌘+N, then **File > Save As**
- Windows/Linux: Ctrl+N, then **File > Save As**

Final structure:

```
myscript/
├── pyproject.toml
├── README.md
└── src/
    └── myscript/
        ├── __init__.py
        └── main.py
```

### 4. Add script logic

In `src/myscript/main.py`, add:

```python
def main():
    print("Hello from myscript!")
```

### 5. Create and activate a virtual environment

Open the terminal:

- macOS: Ctrl+` or **Terminal > New Terminal**
- Windows/Linux: Ctrl+` or **Terminal > New Terminal**

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

- macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

- Windows:
  ```cmd
  .venv\Scripts\activate
  ```

You should now see `(.venv)` in your shell prompt.

### 6. Install in editable mode

With the virtual environment activated:

```bash
pip install -e .
```

Then run:

```bash
myscript
```

You should see:

```
Hello from myscript!
```

### 7. Reinstall if you edit `pyproject.toml`

If you change dependencies, entry points, or metadata in `pyproject.toml`, reinstall:

```bash
pip install -e .
```

### 8. Uninstall the CLI (optional)

```bash
pip uninstall myscript
```

## Use as a template

To reuse this project for other CLI tools:

- Duplicate the folder
- Rename the `myscript` module and CLI command
- Update `pyproject.toml`, `main.py`, and documentation

## References

- [Real Python: Packaging Your Python Code With pyproject.toml (YouTube)](https://www.youtube.com/watch?v=v6tALyc4C10)
- [Real Python: Everyday Project Packaging course](https://realpython.com/courses/packaging-with-pyproject-toml/)
- [Python Packaging Authority (PyPA)](https://packaging.python.org)
- [PEP 517 – Build system abstraction](https://peps.python.org/pep-0517/)
- [PEP 518 – Build dependencies config](https://peps.python.org/pep-0518/)
- [PEP 621 – Standard project metadata](https://peps.python.org/pep-0621/)
- [PEP 660 – Editable installs](https://peps.python.org/pep-0660/)
- [Setuptools + pyproject.toml](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
- [pip build-system reference](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)
- [Semantic Versioning](https://semver.org)