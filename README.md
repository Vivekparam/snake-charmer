# Snake Charmer is in development

## Install dependencies and run

1. [Install pants](https://www.pantsbuild.org/dev/docs/getting-started/installing-pants)
2. `pants generate-lockfiles` to update dependencies
3. `pants export` to export an env
4. `pants run src/core.py` to start.

## Development

`pants lint ::` to lint with ruff
`pants check ::` to run pyright
`pants fix ::` to fix
