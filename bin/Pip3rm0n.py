import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os
import subprocess
import webbrowser  # Import the webbrowser module
import requests


# --- GUI Variables ---
window_title = "Pip3rm0n"
window_size = "450x390"  # Adjusted window size to accommodate progress bar

# Gradient Text Variables
gradient_text = "Pip3rm0n"
font_size = 30  # Adjust this value to change the text size
left_gradient_color = "#73a9ff"  # Left side of gradient
right_gradient_color = "#a30bf4"  # Right side of gradient

# Button and Checkbox Variables
button_start = "START"
button_hack = "Hack a mainframe"
checkbox_rootful = "Rootful"
checkbox_wireful = "Wireful"
checkbox_restore = "Restore RootFS"
checkbox_type = "Semi-untethered (by default, it's untethered)"
checkbox_shell = "iDownload DevShell"
checkbox_cure = "Cure pneumonoultramicroscopicsilicovolcanoconiosis (underrated)"

# Background Colors
window_bg_color = "#141414"  # Dark grey background for the main window
label_bg_color = "#141414"   # Slightly darker grey for the label
button_bg_color = "#151515"  # Light grey for the button
checkbox_bg_color = "#141414"  # A different grey for the checkbox

# Text Colors
label_text_color = "#000000"  # Black text for the label (not used, since we're using an image for the label)
button_text_color = "#ffffff"  # Blue text for the button
checkbox_text_color = "#ffffff"  # Red text for the checkbox
phase_text_color = "#ffffff"  # White text for the phase label

# Progress Bar Variables
phases = [
    "Preparing",
    "Detecting nearby iMobileDevice",
    "Found device 918f9a64-5106-439f-b07b-fe126ca9cecd, patchfinding",
    "Exploiting kernel [WIPL0IT]",
    "Building Phys R/W Primitive",
    "Cleaning up exploits",
    "Elevating Privileges",
    "Updating BaseBin",
    "Extracting Bootstrap",
    "Loading BaseBin TrustCache",
    "Init_JB_Envrmnt",
    "Applying Bind Mount",
    "Finalizing Bootstrap",
    "Zilia Preparing ROOT_PASSWD_CFIRM",
    "Updating Bundled Packages",
    "Checking for duplicate apps"
]
phase_durations = [6000, 5000, 2000, 200, 100, 200, 200, 200, 3000, 500, 5000, 1000, 4000, 200, 200, 500]

# --- Functions ---
def check_internet_connection():
    """Check if the computer is connected to the internet."""
    try:
        # Send a request to a reliable website
        response = requests.get("https://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False



def on_button_click():
    """Handle the button click event."""
    if check_internet_connection():
        start_progress()
    else:
        tk.messagebox.showwarning("No Internet Connection", "You are not connected to the internet.")


def on_hack_click():
    """Handle the 'Hack a mainframe' button click event."""
    exe_path = os.path.join('.', 'tools', 'Ham.exe')
    
    if check_internet_connection():
        if os.path.isfile(exe_path):
            try:
                # Execute the executable
                subprocess.Popen(exe_path, shell=True)
            except Exception as e:
                print(f"An error occurred while trying to run the executable: {e}")
        else:
            messagebox.showerror("File Not Found", f"Executable not found: {exe_path}")
    else:
        messagebox.showwarning("No Internet Connection", "You are not connected to the internet.")

def on_checkbox_toggle():
    """Handle the checkbox toggle event."""
    # No action needed for checkbox toggle
    pass

def create_gradient_text_image(text, font_size, left_color, right_color):
    """Create an image with gradient text."""
    # Create an image with transparent background for the text
    text_width = 400
    text_height = font_size + 20  # Ensure the height is sufficient
    text_image = Image.new('RGBA', (text_width, text_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_image)
    
    # Load TrueType font
    try:
        font = ImageFont.truetype(font_path, font_size)  # Load font with specified size
    except IOError:
        font = ImageFont.load_default()  # Use default font if custom font fails

    # Draw text on a separate image to use as a mask
    text_mask = Image.new('L', (text_width, text_height), 0)
    draw_mask = ImageDraw.Draw(text_mask)
    
    bbox = draw_mask.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (text_image.width - text_width) / 2
    text_y = (text_image.height - text_height) / 2
    draw_mask.text((text_x, text_y), text, font=font, fill=255)

    # Create gradient image
    gradient = Image.new('RGB', (text_image.width, text_image.height), (255, 255, 255))
    draw_gradient = ImageDraw.Draw(gradient)
    
    for x in range(text_image.width):
        r = int((1 - x / text_image.width) * int(left_color[1:3], 16) + (x / text_image.width) * int(right_color[1:3], 16))
        g = int((1 - x / text_image.width) * int(left_color[3:5], 16) + (x / text_image.width) * int(right_color[3:5], 16))
        b = int((1 - x / text_image.width) * int(left_color[5:], 16) + (x / text_image.width) * int(right_color[5:], 16))
        draw_gradient.line([(x, 0), (x, text_image.height)], fill=(r, g, b))

    # Convert gradient image to RGBA mode to match text_image mode
    gradient = gradient.convert('RGBA')

    # Apply gradient to text using mask
    gradient_text_image = Image.new('RGBA', (text_image.width, text_image.height), (255, 255, 255, 0))
    gradient_text_image.paste(gradient, (0, 0), mask=text_mask)

    return gradient_text_image

def start_progress():
    """Start the progress bar and update phases."""
    progress_bar['value'] = 0
    progress_bar['maximum'] = sum(phase_durations)
    update_phase(0)

def update_phase(phase_index):
    """Update the phase and progress bar."""
    if phase_index >= len(phases):
        progress_bar['value'] = progress_bar['maximum']
        phase_label.config(text="Task failed successfully!")
        open_website()  # Call the function to open the website
        return

    # Update the phase label
    phase_label.config(text=phases[phase_index], fg=phase_text_color)
    
    # Update the progress bar
    current_duration = phase_durations[phase_index]
    progress_bar['value'] += current_duration
    root.after(current_duration, update_phase, phase_index + 1)

def open_website():
    """Open the website in the default web browser."""
    webbrowser.open('https://winaviation.github.io/Pip3rm0n/AMOGUS/index.html')

# --- Setup GUI ---
# Create the main window
root = tk.Tk()
root.title(window_title)
root.geometry(window_size)
root.configure(bg=window_bg_color)  # Set the background color of the main window

# Make the window unresizable
root.resizable(False, False)

# Resolve the path to the font
local_app_data_path = os.getenv('LOCALAPPDATA')
font_path = os.path.join(local_app_data_path, 'Microsoft', 'Windows', 'Fonts', 'Nunito-Regular.ttf')

# Create gradient text image
image = create_gradient_text_image(gradient_text, font_size, left_gradient_color, right_gradient_color)

# Convert image to PhotoImage for tkinter
photo = ImageTk.PhotoImage(image)

# Create a label with gradient text image
label = tk.Label(root, image=photo, bg=label_bg_color)  # Set label background color
label.pack(pady=(10, 5))

# Create the progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=350, mode="determinate")
progress_bar.pack(pady=5)

# Create a phase label
phase_label = tk.Label(root, text="", bg=window_bg_color, fg=phase_text_color, font=("Arial", 10))
phase_label.pack(pady=(5, 10))

# Create a button
button = tk.Button(root, text=button_start, command=on_button_click, bg=button_bg_color, fg=button_text_color)  # Set button background and text color
button.pack(pady=5)

button = tk.Button(root, text=button_hack, command=on_hack_click, bg=button_bg_color, fg=button_text_color)  # Set button background and text color
button.pack(pady=5)

# Create a checkbox
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text=checkbox_rootful, variable=checkbox_var, command=on_checkbox_toggle, bg=checkbox_bg_color, fg=checkbox_text_color)  # Set checkbox background and text color
checkbox.pack(pady=1)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text=checkbox_wireful, variable=checkbox_var, command=on_checkbox_toggle, bg=checkbox_bg_color, fg=checkbox_text_color)  # Set checkbox background and text color
checkbox.pack(pady=1)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text=checkbox_restore, variable=checkbox_var, command=on_checkbox_toggle, bg=checkbox_bg_color, fg=checkbox_text_color)  # Set checkbox background and text color
checkbox.pack(pady=1)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text=checkbox_shell, variable=checkbox_var, command=on_checkbox_toggle, bg=checkbox_bg_color, fg=checkbox_text_color)  # Set checkbox background and text color
checkbox.pack(pady=1)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text=checkbox_type, variable=checkbox_var, command=on_checkbox_toggle, bg=checkbox_bg_color, fg=checkbox_text_color)  # Set checkbox background and text color
checkbox.pack(pady=1)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text=checkbox_cure, variable=checkbox_var, command=on_checkbox_toggle, bg=checkbox_bg_color, fg=checkbox_text_color)  # Set checkbox background and text color
checkbox.pack(pady=1)

# Start the GUI event loop
root.mainloop()
