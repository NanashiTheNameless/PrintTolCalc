#!/bin/bash
pipx install --force tox
tox --recreate
tox --recreate -e lint
tox --recreate -e format
