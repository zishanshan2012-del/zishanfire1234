import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Number Pad")
root.geometry("300x400")

# Title
title = tk.Label(root, text="Number Pad", font=("Arial", 20, "bold"))
title.pack(pady=20)

# Create a frame for the number pad
pad_frame = tk.Frame(root)
pad_frame.pack()

# Numbers for the keypad
numbers = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]

# Create the number pad using nested loops
for row in range(4):
    for col in range(3):
        number = numbers[row][col]

        label = tk.Label(
            pad_frame,
            text=number,
            font=("Arial", 24, "bold"),
            width=5,
            height=2,
            relief="raised",
            borderwidth=2
        )

        label.grid(row=row, column=col, padx=5, pady=5)

# Start the application
root.mainloop()