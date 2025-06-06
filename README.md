# Python CLI project packaging with `pyproject.toml`

This guide walks through creating a minimal, standards-compliant Python command-line (CLI) script package with `pyproject.toml`. The project installs in editable mode, allowing the script to run globally during development without needing to rebuild.

The project follows modern Python packaging practices (PEPs 517, 518, 621, 660) and serves as a reusable scaffold for future CLI tools.

Based on: [Packaging Your Python Code With pyproject.toml](https://www.youtube.com/watch?v=v6tALyc4C10) course by Real Python.

## Why use this pattern

- Run your CLI from anywhere using a single command (`snakesay`)—no need to navigate to the script directory or type `python` and the file path every time
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
3. Create a folder named `snakesay`
4. Select and open it

### 2. Add project files

From the **Explorer sidebar**:

- macOS: ⌘+Shift+E
- Windows/Linux: Ctrl+Shift+E

…create two files:

- `pyproject.toml`
- `README.md`

To create a new file:

- macOS: ⌘+N, then ⌘+S to save
- Windows/Linux: Ctrl+N, then Ctrl+S to save

Paste into `pyproject.toml` and save:

```toml
[project]
name = "snakesay"
version = "1.0.0"
description = "Command-line program that prints an ASCII art picture of a snake with a speech bubble containing a given message."
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[project.scripts]
snakesay = "snakesay.__main__:main"

[build-system]
requires = ["setuptools >= 77.0.3"]
build-backend = "setuptools.build_meta"
```

#### What is `pyproject.toml`?

It is the standard project config file used by pip, build, and modern Python tools. It replaces `setup.py`.

- `[build-system]`: Tells pip/setuptools how to build the package.
- `[project]`: Defines metadata, dependencies, and the CLI entry point.
- `[project.scripts]`: Creates and maps a `snakesay` shell command to the `snakesay` package folder and the `__main__.py` module script's `main()` function.

### 3. Create source files

From the Explorer:

- Create a folder: `src/`
- Inside `src/`, create another folder: `snakesay/`
- Inside `src/snakesay/`, create:
  - `__main__.py` (double underscore before and after "main")
  - `snake.py`

Final project structure:

```
snakesay/
├── pyproject.toml
├── README.md
└── src/
    └── snakesay/
        ├── __main__.py
        └── snake.py
```

### 4. Add script logic

In `src/snakesay/__main__.py`, add:

```python
import sys

from snakesay import snake


def main():
    snake.say(" ".join(sys.argv[1:]))


if __name__ == "__main__":
    main()

```

In `src/snakesay/snake.py`, add:

```python
SNAKE = r"""  \
   \    __
    \  {oo}
       (__)\
         λ \\
           _\\__
          (_____)_
         (________)Oo°
"""


def bubble(message: str) -> str:
    """Create a speech bubble for the given message."""
    bubble_length: int = len(message) + 2
    return f"""
 {"_" * bubble_length}
( {message} )    
 {"‾" * bubble_length}"""


def say(message: str) -> None:
    """Print a snake with a speech bubble containing the given message."""
    if not message:
        message = "I never thought I'd say this, but I have nothing to say."
    print(bubble(message))
    print(SNAKE)

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

With the virtual environment activated, run:

```bash
pip install -e .
```

Run the script:

```bash
snakesay
```

You should see:

```console
 ________________________________________________________
(I never thought I'd say this, but I have nothing to say.)
 --------------------------------------------------------
   \    __
    \  {oo}
       (__)\
         λ \\
           _\\__
          (_____)_
         (________)Oo°
```

Try a custom message after the script name:

```bash
snakesay Time is an illusion. Lunchtime doubly so.
```

You should see:

```console
 _________________________________________
(Time is an illusion. Lunchtime doubly so.)
 -----------------------------------------
   \    __
    \  {oo}
       (__)\
         λ \\
           _\\__
          (_____)_
         (________)Oo°
```

### 7. Reinstall the script if you edit `pyproject.toml`

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

Thank you for following along!

## Contributions
  
Contributions are welcome — fork the repo, create a branch, and open a pull request.

Learn more at GitHub’s [Contributing to a project](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)

## References

- [Real Python: Packaging Your Python Code With pyproject.toml](https://www.youtube.com/watch?v=v6tALyc4C10) (YouTube)
- [Python Packaging Authority (PyPA)](https://packaging.python.org)
- [Configuring setuptools using pyproject.toml files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
- [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [pip build-system reference](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)
- [Semantic Versioning](https://semver.org)
- [PEP 517 – Build system abstraction](https://peps.python.org/pep-0517/)
- [PEP 518 – Build dependencies config](https://peps.python.org/pep-0518/)
- [PEP 621 – Standard project metadata](https://peps.python.org/pep-0621/)
- [PEP 660 – Editable installs](https://peps.python.org/pep-0660/)

## License

MIT [LICENSE](LICENSE.md)  
More details: [Choose an open source license](https://choosealicense.com/licenses/mit/)