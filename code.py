import tkinter as tk
from datetime import date
window = tk.Tk()
window.title("Getting started with widgets")
window.geometry("450x350")
heading = tk.Label(window,text = "Welcome!",font =("Arial",20, "bold"))
heading.pack(pady=20)
name_label = tk.Label(window, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=10)
heading.pack(pady=20)

# Name label
name_label = tk.Label(window, text="Enter your name:")
name_label.pack()

# Name entry box
name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=10)


# Function for button click
def greet_user():
    name = name_entry.get()
    today = date.today().strftime("%B %d, %Y")

    if name:
        message = f"Hello, {name}!\nToday is {today}."
    else:
        message = f"Hello!\nToday is {today}."

    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, message)
    output_box.config(state="disabled")


# Button
greet_button = tk.Button(
    window,
    text="Greet Me",
    command=greet_user
)
greet_button.pack(pady=10)

# Text box for dynamic message
output_box = tk.Text(window, height=5, width=40)
output_box.pack(pady=10)

output_box.config(state="disabled")

# Start the GUI
window.mainloop()