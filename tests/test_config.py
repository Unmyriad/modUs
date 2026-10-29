"""Validate the public YAML configuration API."""

import pytest

from modus.config import ConfigError, GeneratorConfig, RunConfig, load_config, save_config


def test_bundled_config_does_not_depend_on_working_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    config = load_config()
    assert config.generator == GeneratorConfig(seed=42)


@pytest.mark.parametrize("content", ["{}", "generator: {}", "generator:\n  seed: null"])
def test_omitted_values_use_generator_defaults(tmp_path, content):
    path = tmp_path / "run.yaml"
    path.write_text(content, encoding="utf-8")
    assert load_config(path) == RunConfig()


def test_custom_settings_round_trip(tmp_path):
    source = tmp_path / "run.yaml"
    source.write_text(
        "generator:\n  problem_size: 12\n  edge_probability: 0.75\n  seed: 123\n",
        encoding="utf-8",
    )
    config = load_config(str(source))
    assert config.generator.model_dump() == {
        "problem_size": 12,
        "edge_probability": 0.75,
        "seed": 123,
    }
    destination = tmp_path / "shared.yaml"
    save_config(config, destination)
    assert load_config(destination) == config


def test_saved_defaults_are_explicit(tmp_path):
    path = tmp_path / "defaults.yaml"
    save_config(RunConfig(), path)
    assert "seed: null" in path.read_text(encoding="utf-8")
    assert load_config(path) == RunConfig()


@pytest.mark.parametrize(
    "content",
    [
        "",
        "null",
        "[]",
        "hello",
        "generator: [",
        "generator: null",
        "generator:\n  problem_size: 0",
        "generator:\n  problem_size: -1",
        "generator:\n  problem_size: true",
        'generator:\n  problem_size: "20"',
        "generator:\n  problem_size: 1.5",
        "generator:\n  edge_probability: -0.1",
        "generator:\n  edge_probability: 1.1",
        "generator:\n  edge_probability: .nan",
        "generator:\n  edge_probability: true",
        'generator:\n  seed: "42"',
        "generator:\n  seed: false",
        "generator:\n  node_size: 20",
        "generatr: {}",
        "!!python/object/apply:os.system ['echo unsafe']",
    ],
)
def test_invalid_configuration_reports_source(tmp_path, content):
    path = tmp_path / "invalid.yaml"
    path.write_text(content, encoding="utf-8")
    with pytest.raises(ConfigError, match="invalid.yaml"):
        load_config(path)


def test_missing_file_reports_source(tmp_path):
    with pytest.raises(ConfigError, match="missing.yaml"):
        load_config(tmp_path / "missing.yaml")


def test_invalid_encoding_reports_source(tmp_path):
    path = tmp_path / "invalid.yaml"
    path.write_bytes(b"\xff")
    with pytest.raises(ConfigError, match="invalid.yaml"):
        load_config(path)


def test_save_failure_reports_destination(tmp_path):
    with pytest.raises(ConfigError, match="run.yaml"):
        save_config(RunConfig(), tmp_path / "missing" / "run.yaml")
