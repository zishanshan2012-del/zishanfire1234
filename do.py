import tkinter as tk

root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")

    label = tk.Label(
        new_window,
        text="Welcome to the New Window!",
        font=("Arial", 14)
    )
    label.pack(pady=50)

button = tk.Button(
    root,
    text="Open a new window",
    font=("Arial", 14),
    command=open_new_window
)
button.pack(pady=100)

root.mainloop()