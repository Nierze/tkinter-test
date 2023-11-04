import tkinter as tk
from tkinter import ttk
import ctypes

# idk what this do
myappid = "mycompany.myproduct.subproduct.version"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# window
window = tk.Tk()
window.title("Test")
window.geometry("1080x720")
window.iconbitmap('testIcon.ico')

# title
test_title = ttk.Label(master=window, text='Sex', font=("century gothic", 32, "italic", "underline", "bold"))
test_title2 = ttk.Label(master=window, text='Sex2', font=("century gothic", 32, "italic", "underline", "bold"))
test_title.pack()
test_title2.pack()
# run
window.mainloop()



















