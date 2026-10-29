"""Load and share validated YAML run configurations without import-time file I/O."""

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

DEFAULT_CONFIG_PATH = Path(__file__).with_name("config.yaml")


class ConfigError(ValueError):
    """A configuration file cannot be read, validated, or written."""


class GeneratorConfig(BaseModel):
    """Arguments accepted by ``generate_max_cut``."""

    model_config = ConfigDict(extra="forbid", strict=True, validate_assignment=True)

    problem_size: int = Field(default=20, ge=1)
    edge_probability: float = Field(default=0.5, ge=0.0, le=1.0)
    seed: int | None = None


class RunConfig(BaseModel):
    """Settings for a project run; omitted settings use generator defaults."""

    model_config = ConfigDict(extra="forbid", strict=True, validate_assignment=True)

    generator: GeneratorConfig = Field(default_factory=GeneratorConfig)


def load_config(path: str | Path = DEFAULT_CONFIG_PATH) -> RunConfig:
    """Read a YAML mapping and validate its settings.

    Relative paths resolve from the working directory. With no path, load the
    bundled example beside this module. An explicit ``{}`` uses all defaults;
    empty files, unknown keys, and invalid values raise ``ConfigError``.
    """
    path = Path(path)
    try:
        with path.open(encoding="utf-8") as stream:
            data = yaml.safe_load(stream)
        return RunConfig.model_validate(data)
    except (OSError, UnicodeError, yaml.YAMLError, ValidationError) as exc:
        raise ConfigError(f"Could not load configuration '{path}': {exc}") from exc


def save_config(config: RunConfig, path: str | Path) -> None:
    """Write all settings, including defaults, to a shareable YAML file.

    An existing destination is overwritten. Its parent directory must exist.
    """
    path = Path(path)
    try:
        data = RunConfig.model_validate(config.model_dump()).model_dump(mode="json")
        content = yaml.safe_dump(data, sort_keys=False)
        path.write_text(content, encoding="utf-8")
    except (OSError, UnicodeError, yaml.YAMLError, ValidationError) as exc:
        raise ConfigError(f"Could not save configuration '{path}': {exc}") from exc
