# Python CLI project packaging with `pyproject.toml`

This guide walks through creating a minimal, standards-compliant Python command-line (CLI) script package with `pyproject.toml`. The project installs in editable mode, allowing the script to run globally during development without needing to rebuild.

The project follows modern Python packaging practices (PEPs 517, 518, 621, 660) and serves as a reusable scaffold for future CLI scripts.

Based on: [Packaging Your Python Code With pyproject.toml](https://www.youtube.com/watch?v=v6tALyc4C10) course by Real Python.

## Why use this pattern?

Pros:

- Run your CLI script from anywhere using only the script name—no need to navigate to the script directory, enter the script path, or type `python` before the script name
- Follow Python packaging standards (`pyproject.toml`, editable installs)
- Avoid rebuilds after changes
- Integrate easily with IDEs, CI, and deployment tools

Cons:

- You’ll need to run scripts manually (`python file.py`)
- Structure may not support packaging or distribution
- Tooling (e.g. Poetry, build, pip) may not detect your project

## What is `pyproject.toml`?

`pyproject.toml` is the standard project configuration file used by pip, build, and modern Python tools. It replaces `setup.py`.

- `[build-system]`: Tells pip/setuptools how to build the package.
- `[project]`: Defines metadata, dependencies, and CLI script entry point.
- `[project.scripts]`: Creates and maps a `snakesay` shell command to the `snakesay` package folder and the `__main__.py` module script's `main()` function.

See the References section to learn more.

## Quick start

Follow these steps to quickly set up and try out the example CLI project. You’ll clone the repository, create a virtual environment, install the package in editable mode, and run the CLI script from anywhere in your terminal.

```bash
git clone https://github.com/nite-stocker/python-cli-package-pyproject
cd python-cli-package-pyproject
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
snakesay Hello, World!
```

Carry on to the Guide for a walkthrough of the full project setup and packaging process.

## Guide

### 1. Project structure

Create the project folder structure and files:

```bash
snakesay-project/
├── pyproject.toml
├── README.md
└── src/
    └── snakesay/
        ├── __main__.py
        └── snake.py
```

### 2. Configuration

Insert the below TOML tables into `pyproject.toml`.

The `[build-system]` table tells tools like `pip` how to build your project, using the setuptools build system. The `[project]` table defines your package’s name, version, dependencies, minimum Python version, and command-line entry point.

```toml
[project]
name = "snakesay"
version = "1.0.0"
description = "CLI script that prints an ASCII art picture of a snake with a speech bubble containing a given message."
requires-python = ">=3.10"
dependencies = []

[project.scripts]
ssnakessay = "snakesay.__main__:main"

[build-system]
requires = ["setuptools >= 77.0.3"]
build-backend = "setuptools.build_meta"
```

### 3. Script logic

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

### 4. Project isolation

Create a virtual environment to keep your project isolated so installs don’t affect other projects or Python versions:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

- macOS/Linux: `source .venv/bin/activate`
- Windows: `.venv\Scripts\activate`

You should now see `(.venv)` in your shell prompt.

### 5. Install the project in editable mode

Editable mode installs the project so code changes take effect immediately during development—no need to reinstall after edits.

With the virtual environment activated, run:

```bash
pip install -e .
```

The "." tells `pip` to install the package defined in the current folder.

### 6. Run the script

In your terminal, run:

```bash
snakesay
```

You should see:

```bash
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

### 7. Reinstall the script after editing `pyproject.toml`

If you revise dependencies, entry points, or metadata in `pyproject.toml`, the script must be reinstalled to apply the changes. Let's demonstrate this by renaming the entry-point script name.

In `pyproject.toml` under the `[project.scripts]` table header, add a couple extra "S"s to the script name:

```toml
[project.scripts]
ssnakessay = "snakesay.__main__:main"
```

Re-install the script:

```bash
pip install -e .
```

Run the script with its new name:

```bash
ssnakessay
```

### 8. Uninstall the CLI script (optional)

```bash
pip uninstall ssnakessay
```

### 9. Use this project as a scaffold

To reuse this project for other CLI script projects:

1. Deactivate the virtual environment (macOS/Linux/Windows): `deactivate`
2. Delete the .venv virtual environment folder
3. Duplicate the `snakesay-project` folder and rename to `python-package-scaffold`
4. Generalize the structure naming, configuration, and script code as much as you need for project quick starts

### Thank you for following along!

## Contributions
  
Contributions are welcome — fork the repo, create a branch, and open a pull request.

Learn more at GitHub’s [Contributing to a project](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)

## References

### Course this guide is based on

- [Real Python: Packaging Your Python Code With pyproject.toml](https://www.youtube.com/watch?v=v6tALyc4C10) (YouTube)

### Packaging

- [Python Packaging User Guide)](https://packaging.python.org/en/latest/)
- [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

### Build system

- [Configuring setuptools using pyproject.toml files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)    
- [pip build-system reference](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)

### Standards

- [PEP 517 – Build system abstraction](https://peps.python.org/pep-0517/)
- [PEP 518 – Build dependencies config](https://peps.python.org/pep-0518/)
- [PEP 621 – Standard project metadata](https://peps.python.org/pep-0621/)
- [PEP 660 – Editable installs](https://peps.python.org/pep-0660/)

### Extra

- [Semantic Versioning](https://semver.org)

## License

MIT [LICENSE](LICENSE.md)  
More details: [Choose an open source license](https://choosealicense.com/licenses/mit/)