#!/usr/bin/env bash
if [[ "$OSTYPE" == "darwin"* ]]; then
    # MacOS
    echo "$HOME/Desktop"
elif [[ "$OSTYPE" == "cygwin" ]] ||
     [[ "$OSTYPE" == "msys" ]] ||
     [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    PowerShell.exe '[Environment]::GetFolderPath("Desktop")'
elif [[ "$(uname -r)" == *"microsoft"* ]] ; then
    # WSL
    PowerShell.exe '[Environment]::GetFolderPath("Desktop")'
else
    xdg-user-dir DESKTOP
fi