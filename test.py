import tkinter as tk
import os
import pyautogui

def on_checkbox_toggle():
    if checkbox_var.get() == 1:
        pyautogui.keyDown('f20')
        pyautogui.keyUp('f20')
    else:
        pyautogui.keyDown('f20')
        pyautogui.keyUp('f20')
        

# Create the main Tkinter window
root = tk.Tk()
root.title("Toggle Key Press")


def on_close():
            # Terminate the 'woah.exe' process when the Tkinter window is closed
            os.system("taskkill /f /im woah.exe")
            root.destroy()

        # Configure the Tkinter window to call 'on_close' when closed
root.protocol("WM_DELETE_WINDOW", on_close)


# Create a Checkbox
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Toggle Glow", variable=checkbox_var, command=on_checkbox_toggle)
checkbox.pack(pady=10)
checkbox_var.set(1)

root.attributes('-topmost', True)
root.mainloop()
