# Contribution guide

This project is open source.
All contributions are welcome.

## Set up development environment

This project uses [`uv`](https://docs.astral.sh/uv/) for package and tool management
and [`nox`](https://nox.thea.codes/en/stable/index.html) to define tasks,
such as building the docs or running tests.

To install `nox` with `uv`, run:

```sh
uv tool install nox
```

## Run sessions

To list the available sessions, run: `nox -ls`.
To run a specific session, run: {samp}`nox -s {SESSION}`,
append `-p 3.13` to run the session only with the latest supported Python version.

For example, to build the docs with Python 3.13 and start a server for a live preview, run:

```sh
nox -s docs -p 3.13 -- --live
```
