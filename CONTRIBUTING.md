# Contribution guide

This project is open source.
All contributions are welcome.

## Set up development environment (fast)

If you just want to edit the docs, or make a few small changes to the code,
and you have Python 3.8, 3.9, 3.10, 3.11, or 3.12 installed,
run these commands to install the dependencies:

```sh
pip install -U nox poetry

# Run nox session, for example, to build the docs
nox -s docs -p 3.12
```

Replace the Python version with the one that's installed on your system.

## Set up development environment (reproducible, isolated)

It's best if you set up a reproducible development environment,
where all applications are as isolated as possible.

1. To run specific versions of Python, install a Python version manager,
   such as `pyenv` or `mise`.

1. Install a specific Python version, for example, with `mise`:

   ```sh
   mise install python@3.12
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

## Tools

This project uses [Poetry](https://python-poetry.org/) to build Python packages and manage dependencies.

This project uses [Nox](https://nox.thea.codes/en/stable/) to run tasks,
such as linting, testing, and building the docs,
in isolated virtual environments.
This makes running these tasks more predictable.
All asks are defined in the file `noxfile.py` as _sessions_.

To get an overview over all defined sessions, run `nox -ls`.
To run a specific session, run {samp}`nox -s {SESSION}`.

To build the docs and start a development server, run `nox -s docs -p 3.12 -- --live`.
