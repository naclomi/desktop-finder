#!/usr/bin/env bash
if [[ "$OSTYPE" == "darwin"* ]]; then
    # MacOS
    echo "$HOME/Desktop"
elif [[ "$OSTYPE" == "cygwin" ]] ||
     [[ "$OSTYPE" == "msys" ]] ||
     [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    echo $(PowerShell.exe '[Environment]::GetFolderPath("Desktop")')
elif [[ "$(uname -r)" == *"microsoft"* ]] ; then
    # WSL
    echo $(PowerShell.exe '[Environment]::GetFolderPath("Desktop")')
else
    echo $(xdg-user-dir DESKTOP)
fi