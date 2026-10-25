<h1>
    <img alt="Modus Logo" src="./assets/modus.png" width=1000 valign="middle">
</h1>


<center> modus provides a command-line tool that generates and solves Max-Cut combinatorial problems on CPU, GPU, and IBM Quantum Cloud</center>

# Features

-  5 way Max-Cut solution:
    - CPU
    - GPU (*Nvidia cQuantum*)
    - Qiskit Simulator (CPU and GPU)
    - IBM Quantum Cloud (*Physical QPU*)
- REST API endpoint provided by [FastAPI](https://fastapi.tiangolo.com/)
- YAML configuration
- JSON Output

# Installation
The project is created using a UNIX-Like or UNIX shell (Linux, macOS, WSL2), naturally to install it will be the same. It's also managed using [uv](https://docs.astral.sh/uv/) which must be installed beforehand.

## Step 1 - Install UV
This project uses [uv](https://docs.astral.sh/uv/) as it's environment and package manager due to its speed and ease of use, install it before proceeding:

### macOS
install via [Homebrew](https://brew.sh) or [MacPorts](https://www.macports.org/)
```bash
# Homebrew
brew install uv
# MacPorts
sudo port install
```
### Linux and WSL2
```bash
## Debian/Ubuntu
sudo apt install uv
# Arch
sudo pacman -S uv
# Fedora
sudo dnf install uv
```

### Verify Installation
```bash
uv --version
```
## Step 2
Clone this repo
```bash
git clone https://github.com/unmyriad/modus.git
cd modus
```
## Step 3 - Choose a hardware group
modus has two **mutually exclusive** dependency groups. Pick the one that matches your machine:

| Group | Use when | Methods available |
|-------|----------|-------------------|
| `gpu` | You have an NVIDIA GPU (Linux x86_64 or WSL2) | All 5: Classical CPU, Classical GPU, Qiskit CPU, Qiskit GPU, IBM Quantum |
| `cpu` | No NVIDIA GPU (laptops, macOS, CI) | Classical CPU, Qiskit CPU, IBM Quantum |

```bash
# NVIDIA GPU machine
uv sync --no-dev --locked --group gpu

# CPU-only machine
uv sync --no-dev --locked --group cpu
```

> [!NOTE]
> The `gpu` group also includes the CPU simulator (`qiskit-aer-gpu` supports `device="CPU"`), so on a GPU machine you only ever need `--group gpu`.

### Why can't I install both groups?
`qiskit-aer` (CPU) and `qiskit-aer-gpu` (GPU) are two builds of the **same library**. Both install into the same `qiskit_aer/` folder and are imported the same way (`import qiskit_aer`). If both were installed, one would overwrite the other's files, and uninstalling either would break the other. Python can't keep two packages with the same import name side by side, so `pyproject.toml` declares the groups as conflicting and uv refuses to install them together.

### Why does `uv sync` remove the other group?
`uv sync` is **exact** by design: it makes your `.venv` match exactly what `uv.lock` and your command describe, and removes anything else. This keeps environments reproducible, because no leftover packages make code work on one machine but not another.

| Command | Result |
|---------|--------|
| `uv sync --group gpu` | Installs the GPU packages and removes `qiskit-aer` if present |
| `uv sync --group cpu` | Installs `qiskit-aer` and removes the GPU packages if present |
| `uv sync --group cpu --group gpu` | Refused (conflicting groups) |
| `uv sync` *(no group)* | ⚠️ Removes **both** hardware groups |
| `uv run ...` | Never removes packages. Safe to use after syncing a group. |

> [!WARNING]
> A bare `uv sync` (e.g. after `git pull`) will remove your hardware group. Always pass your group (`uv sync --group gpu`), or use `uv sync --inexact` to add new packages without removing any.

After switching groups, check which Aer build is active:
```bash
uv run python -c "import qiskit_aer; print(qiskit_aer.__version__)"
```

For dev packages, check [Development](#development)


# Usage
modus can be ran using UV, to do this:

```bash
cd modus
uv run modus
```

# Development
Development tools (`pytest`, `ruff`, `mypy`) are in the `dev` group, which uv installs by default. Add your hardware group as usual:
```bash
uv sync --group gpu                 # or --group cpu
uv sync --group gpu --group docs    # include Sphinx to build the documentation
```
