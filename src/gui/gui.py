import tkinter as tk
from src.svg_to_png.converter import convert_button_click

# Create GUI window
window = tk.Tk()
window.title("SVG to WEBP Converter")

# Add convert button
convert_button = tk.Button(window, text="Convert SVG to WEBP", command=convert_button_click)
convert_button.pack()
