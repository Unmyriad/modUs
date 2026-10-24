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
To sync packages between `pyproject.toml` and `uv.lock` for the user group only using uv, run:
```bash
uv sync --no-dev --locked
```
For dev packages, check [Development](#development)


# Usage
modus can be ran using UV, to do this:

```bash
cd modus
uv run modus
```

# Development
