import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import os

def open_file():
    file_path = filedialog.askopenfilename()
    return file_path

def add_watermark(file_path, watermark_text, output_dir):
    try:
        original_image = Image.open(file_path)
        width, height = original_image.size
        original_image.show()

        # Create a copy of the original image
        watermark_image = original_image.copy()

        draw = ImageDraw.Draw(watermark_image)
        w, h = original_image.size
        x, y = int(w / 2), int(h / 2)
        font_size = min(x, y) // 6

        # Choose a stylish font (you can replace "arial.ttf" with your preferred font file)
        font_path = "path_to_your_font_file.ttf"  # Update with the path to your font file
        font = ImageFont.truetype(font_path, font_size)

        # Add Watermark in a stylish way
        draw.text((x, y), watermark_text, fill=(255, 255, 255), font=font, anchor='ms')

        # Create a 'watermarked' folder next to main.py
        output_dir = os.path.join(os.path.dirname(__file__), 'watermarked')
        os.makedirs(output_dir, exist_ok=True)

        # Save the watermarked image in the 'watermarked' folder
        output_path = os.path.join(output_dir, "watermarked_image.png")
        watermark_image.save(output_path)
        return output_path
    except Exception as e:
        return str(e)

def browse_and_watermark():
    file_path = open_file()
    if file_path:
        watermark_text = watermark_entry.get()
        output_path = add_watermark(file_path, watermark_text, os.path.dirname(file_path))
        result_label.config(text=f"Watermarked image saved as:\n{output_path}", fg="#28A745")  # Green color for success

# Create the main window
root = tk.Tk()
root.title("Image Watermark Tool")
root.geometry("400x300")  # Set the initial window size

# Configure GUI elements with styles
label = tk.Label(root, text="Enter Watermark Text:", font=("Arial", 14), bg="#F0F0F0")
label.pack(pady=10)

watermark_entry = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid")
watermark_entry.pack(pady=10)

browse_button = tk.Button(root, text="Browse and Add Watermark", command=browse_and_watermark, font=("Arial", 12), bd=2, relief="solid", bg="#007BFF", fg="#FFFFFF")
browse_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12), fg="#DC3545")  # Red color for error
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
