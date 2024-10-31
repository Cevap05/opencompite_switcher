import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Define the directory where the file will be replaced
TARGET_DIRECTORY = "E:\\SteamLibrary\\steamapps\\common\\assettocorsa\\system\\x64"  # Replace with your target directory path
TARGET_FILENAME = "openvr_api.dll"  # The target file name, always "openvr_api.dll"

# Define the source file paths
SteamVR_PATH = "SteamVR.dll"  # Replace with the actual path of SteamVR's DLL file
OpenComposite_PATH = "OpenComposite.dll"  # Replace with the actual path of OpenComposite's DLL file

# Function to replace the file with SteamVR's DLL
def replace_with_steamvr():
    try:
        shutil.copy(SteamVR_PATH, os.path.join(TARGET_DIRECTORY, TARGET_FILENAME))
        messagebox.showinfo("Success", f"'{TARGET_FILENAME}' has been replaced with SteamVR's file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to replace the file with OpenComposite's DLL
def replace_with_opencomposite():
    try:
        shutil.copy(OpenComposite_PATH, os.path.join(TARGET_DIRECTORY, TARGET_FILENAME))
        messagebox.showinfo("Success", f"'{TARGET_FILENAME}' has been replaced with OpenComposite's file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("AC Switcher")
window.geometry("300x200")

# Create and place the buttons
button_steam_vr = tk.Button(window, text="SteamVR", command=replace_with_steamvr)
button_steam_vr.pack(pady=20)

button_open_composite = tk.Button(window, text="OpenComposite", command=replace_with_opencomposite)
button_open_composite.pack(pady=20)

# Run the main loop
window.mainloop()
