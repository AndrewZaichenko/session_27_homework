#!/bin/bash
# Python and pip should be installed at this point

EGG_INFO_DIR="*.egg-info"
VENV_NAME="hillel_venv"
PYTHON_ALIAS="python"

echo "Removing existing log temporary files"
rm -rf .*.log
rm -rf ${EGG_INFO_DIR}

echo "Removing existing virtualenv directory <$VENV_NAME>"
rm -rf $VENV_NAME

echo "Removing pytest_cache"
rm -rf .pytest_cachepwd

echo "Creating a new virtualenv <$VENV_NAME>"
type -P $PYTHON_ALIAS >/dev/null 2>&1
rc=$?

if [[ $rc == 1 ]]; then
  PYTHON_ALIAS="python"
fi
echo "virtualenv command: $PYTHON_ALIAS -m virtualenv $VENV_NAME"
$PYTHON_ALIAS -m pip install virtualenv
$PYTHON_ALIAS -m virtualenv $VENV_NAME

echo "Virtual environment initialization"

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        set +u
        source "$VENV_NAME/bin/activate"
        set -u
elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX
        source "$VENV_NAME/bin/activate"
elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
        source "$VENV_NAME/Scripts/activate"
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
        source "$VENV_NAME/Scripts/activate"
elif [[ "$OSTYPE" == "win32" ]]; then
        # I'm not sure this can happen.
        source "$VENV_NAME/Scripts/activate"
else
        echo "Unknown OS found. Script will be exit"
        exit 1
fi
echo "Installing environment dependencies ..."

pip install -r requirements.txt
pip install -e .
echo "All done"