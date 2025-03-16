import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Textfiles", ".txt")])

    if not filepath:
        return
    
    text_edit.delete(1.0,tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Textfiles", ".txt")])
    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")

def main():
    window = tk.Tk()

    window.title("Notepad--")
    window.geometry("1230x650")
    window.columnconfigure(0, weight=1)


    text_edit = tk.Text (window, font = "Helvetica 18")
    text_edit.grid(row = 1, sticky="ew")

    frame = tk.Frame(window, relief = tk.RAISED, bd = 2)
    save_btn = tk.Button (frame,text = "Save", command = lambda: save_file(window, text_edit))
    open_btn = tk.Button (frame, text = "Open", command = lambda: open_file(window, text_edit))

    save_btn.grid(row = 0, column = 1, padx=5, pady=5,sticky="ew")
    open_btn.grid(row = 0, column = 0, padx=5, pady=5, sticky="ew")
    frame.grid(row = 0, sticky="ew")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.mainloop()

main()