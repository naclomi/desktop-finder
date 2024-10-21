#!/usr/bin/env bash
if [[ "$OSTYPE" == "darwin"* ]]; then
    # MacOS
    ABS_DESKTOP="$HOME/Desktop"
    POSIX_DESKTOP="$ABS_DESKTOP"
elif [[ "$OSTYPE" == "cygwin" ]] ||
     [[ "$OSTYPE" == "msys" ]] ||
     [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    ABS_DESKTOP=$(PowerShell.exe '[Environment]::GetFolderPath("Desktop")')
    POSIX_DESKTOP=$(cygpath "$ABS_DESKTOP")
elif [[ "$(uname -r)" == *"microsoft"* ]] ; then
    # WSL
    ABS_DESKTOP=$(PowerShell.exe '[Environment]::GetFolderPath("Desktop")')
    POSIX_DESKTOP=$(wslpath "$ABS_DESKTOP")
else
    # Linux
    ABS_DESKTOP=$(xdg-user-dir DESKTOP)
    POSIX_DESKTOP="$ABS_DESKTOP"
fi

if [[ $* == *--abs* ]]; then
    echo "$ABS_DESKTOP"
else
    REL_DESKTOP=$(realpath -s --relative-to="." "$POSIX_DESKTOP")
    echo "$REL_DESKTOP"
fi