import tkinter
from tkinter.ttk import Labelframe
import os
from os import stat_result

root = tkinter.Tk()
root.title('ENG')
root.configure(background='cyan')


def cmd():
    root2 = tkinter.Tk()
    path = 'c:/users/pc/desktop/courses'
    os.system('cd' + ' ' + str(path))
    root2.mainloop()


frame = Labelframe(root, text='DICTIONARY >~<')
frame.pack(padx=200, pady=200)
button = tkinter.Button(frame, text='Download', padx=5, pady=5, command=cmd).pack(padx=60, pady=60)
root.mainloop()
