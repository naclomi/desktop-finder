#!/usr/bin/env python3
import sys
import tkinter

if __name__=="__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = sys.stdin.read()

    root = tkinter.Tk()
    root.title('Desktop Finder')
    root.geometry("400x175")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    ui_font = ("Terminal", 16)
    w = tkinter.Text(root, height=2, borderwidth=0, padx=10, pady=10, wrap=tkinter.CHAR, font=ui_font)
    w.insert(1.0, path)
    w.grid(row=0, column=0, columnspan=2, sticky="news")
    w.configure(state="disabled")
    w.configure(inactiveselectbackground=w.cget("selectbackground"))

    def copyCallBack():
        root.clipboard_clear()
        root.clipboard_append(path)
        root.update()

    copy_button = tkinter.Button(root, text="Copy", command=copyCallBack, font=ui_font)
    copy_button.grid(row=1, column=0, ipadx=30, ipady=10, padx=10, pady=10)

    exit_button = tkinter.Button(root, text="Close", command=root.destroy, font=ui_font)
    exit_button.grid(row=1, column=1, ipadx=30, ipady=10, padx=10, pady=10)

    root.mainloop()