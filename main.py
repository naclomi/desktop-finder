#!/usr/bin/env python3
import platform
import sys

os_family = platform.system()

if os_family == "Windows":
    # Windows

    def _windowsDesktopPath():
        try:
            # Uses pythonnet
            import clr
            from System import Environment
            return Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory)
        except:
            try:
                # Uses pywin32
                from win32comext.shell import shell
                return shell.SHGetKnownFolderPath(shell.FOLDERID_Desktop)
            except:
                import subprocess
                return subprocess.check_output(['PowerShell.exe', '[Environment]::GetFolderPath("Desktop")']).decode("utf-8").rstrip()                
    def findDesktopPath():
        return _windowsDesktopPath()
elif os_family == "Linux":
    if "microsoft" in platform.uname().release.lower():
        # WSL
        def findDesktopPath():
            import subprocess
            return subprocess.check_output(['PowerShell.exe', '[Environment]::GetFolderPath("Desktop")']).decode("utf-8").rstrip()
    else:
        # True Linux
        def findDesktopPath():
            import subprocess
            return subprocess.check_output(['xdg-user-dir', 'DESKTOP']).decode("utf-8").rstrip()
elif os_family == "Darwin":
    # TODO
    raise NotImplementedError()

if __name__=="__main__":
    # if sys.stdin and sys.stdin.isatty():
    #     print(findDesktopPath())
    # else:
    import tkinter
    root = tkinter.Tk()
    root.title('Desktop Finder')
    root.geometry("400x175")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    ui_font = ("Terminal", 16)
    w = tkinter.Text(root, height=2, borderwidth=0, padx=10, pady=10, wrap=tkinter.CHAR, font=ui_font)
    w.insert(1.0, findDesktopPath())
    w.grid(row=0, column=0, columnspan=2, sticky="news")
    w.configure(state="disabled")
    w.configure(inactiveselectbackground=w.cget("selectbackground"))

    def copyCallBack():
        root.clipboard_clear()
        root.clipboard_append(findDesktopPath())
        root.update()

    copy_button = tkinter.Button(root, text="Copy", command=copyCallBack, font=ui_font)
    copy_button.grid(row=1, column=0, ipadx=30, ipady=10, padx=10, pady=10)

    exit_button = tkinter.Button(root, text="Close", command=root.destroy, font=ui_font)
    exit_button.grid(row=1, column=1, ipadx=30, ipady=10, padx=10, pady=10)

    root.mainloop()