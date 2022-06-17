#!/bin/sh

python3 -m venv local_lib
source local_lib/bin/activate

pip3 install --upgrade --quiet --force-reinstall --disable-pip-version-check --target=local_lib git+https://github.com/jaraco/path.git --log my_log.log 

pip3 --version

python3 my_program.py