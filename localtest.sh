#!/bin/bash
pipx install --force tox
tox --verbose --recreate
tox --verbose --recreate -e lint
tox --verbose --recreate -e format