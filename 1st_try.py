import tkinter as tk

def on_button_click():
    label.config(text="Hello, World!")

# create main window
root = tk.Tk()
root.title("Simple App")

# create a label
label = tk.Label(root, text="按下按鈕")
label.pack()

# create a button
button = tk.Button(root, text="點我", command=on_button_click)
button.pack()

# run the app
root.mainloop()
