import tkinter as tk

def on_button_click():
    label.config(text="Hello, World!")

# create main window
root = tk.Tk()
root.title("Sakamichi member's blog")

#get the width,height of computer's screen
#so that window can show at its center
window_width = 1200
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() - 40 #minus the height(40 or 75) of taskbar below the screen
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
#set W,H of the window
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# create a label
label = tk.Label(root, text="按下按鈕")
label.pack()

# create a button
button = tk.Button(root, text="點我", command=on_button_click)
button.pack()

# run the app
root.mainloop()
