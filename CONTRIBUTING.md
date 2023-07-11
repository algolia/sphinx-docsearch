# Contribution guide

This project is open source. All contributions are welcome.

## Set up development environment (fast)

If you just want to edit the docs, or make a few small changes to the code,
and you have Python 3.8, 3.9, 3.10, or 3.11 installed,
run these commands to install the dependencies:

```sh
pip install -U nox poetry

# Run nox session, e.g., to build the docs
nox -s docs -p 3.11
```

Replace the Python version with the one that's installed on your system.

## Set up development environment (reproducible, isolated)

It's best if you set up a reproducible development environment,
where all applications are as isolated as possible.

1. To run specific versions of Python, install a Python version manager,
   such as `pyenv` or `rtx`.

1. Install the latest supported Python version, 3.11, for example, with `rtx`:

   ```sh
   rtx install python@3.11
   ```

1. Specify a Python version, either locally or globally.

1. Install `pipx` to install Python applications into isolated environments.

   ```sh
   pip install -U pipx
   ```

1. Install `Poetry` and `Nox`:

   ```sh
   pipx install poetry
   pipx install nox
   ```

- `nox -ls`: list all sessions
- `nox -s <SESSION>`: run session with name _`<NAME>`_.
- `nox -s docs -p 3.11 -- --live`: build the docs and start development web server.
