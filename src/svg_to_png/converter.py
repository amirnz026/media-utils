from tkinter import filedialog
import cairosvg
from ffmpy import FFmpeg
import os


def convert_to_webp(png_file, webp_file):
    ff = FFmpeg(inputs={png_file: None}, outputs={webp_file: None})
    ff.run()
    print(f"Conversion successful: {webp_file}")


def convert_to_png(svg_file, png_file):
    with open(svg_file, 'r') as f:
        svg_data = f.read()
    png_data = cairosvg.svg2png(bytestring=svg_data,scale=1.5)
    with open(png_file, 'wb') as f:
        f.write(png_data)
    print(f"Conversion successful: {png_file}")

def convert_button_click():
    svg_files = filedialog.askopenfilenames(filetypes=[("SVG Files", "*.svg")])
    for svg_file in svg_files:
        png_file = svg_file[:-4] + ".png"
        convert_to_png(svg_file, png_file)
        webp_file = svg_file[:-4] + ".webp"
        convert_to_webp(png_file, webp_file)
        os.remove(png_file)
