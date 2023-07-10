# Contribution guide

This project is open source.

## Set up development environment

## Python

- `pyenv`, `rtx`
- `rtx install python@3.11`
- `rtx use -g python@3.11`

- `pip install -U pipx`
- `pipx install poetry nox`

Nox:

- `nox -ls`: list all sessions
- `nox -s <SESSION>`: run session with name _`<NAME>`_.
- `nox -s docs -p 3.11 -- --live`: build the docs and start development web server.
