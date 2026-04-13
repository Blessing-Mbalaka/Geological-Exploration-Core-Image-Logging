import os
import pandas as pd
from tkinter import Tk, filedialog, Label, Button, PhotoImage

# Global variable to store selected image files
selected_images = []

def import_images():
    global selected_images
    selected_images = filedialog.askopenfilenames(
        title="Select Image Files",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")],
    )
    status_label.config(text=f"{len(selected_images)} images selected")

def import_excel():
    if not selected_images:
        status_label.config(text="Please select images first.")
        return

    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        process_excel(file_path)

def process_excel(file_path):
    # Load Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Get image directory
    image_directory = os.path.dirname(selected_images[0])

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        from_distance = row['From']
        to_distance = row['To']

        # Construct the new file name based on the distance ranges
        new_name = f"[{from_distance}_to_{to_distance}].jpg"

        # Check if the image files exist in the selected images
        for image_file in selected_images:
            image_name = os.path.basename(image_file)
            if image_name.startswith(f"image_{index + 1}"):
                # Build the full paths for the old and new names
                old_path = os.path.join(image_directory, image_name)
                new_path = os.path.join(image_directory, new_name)

                # Rename the file
                os.rename(old_path, new_path)

    status_label.config(text="Photos renamed successfully!")

# GUI setup
root = Tk()
root.title("Kweneng Core Photo Renamer")
root.geometry("400x300")  # Set a specific window size

# Load the provided logo
logo_image = PhotoImage(file=r"C:\Users\bjmba\Downloads\cropped-Kwenwng-logo.png")
logo_label = Label(root, image=logo_image)
logo_label.pack()

import_images_button = Button(root, text="Select Images", command=import_images, bg="#405DE6", fg="white", font=("Helvetica", 12))
import_images_button.pack(pady=10)

import_excel_button = Button(root, text="Select Excel", command=import_excel, bg="#405DE6", fg="white", font=("Helvetica", 12))
import_excel_button.pack(pady=10)

status_label = Label(root, text="", font=("Helvetica", 12))
status_label.pack()

root.mainloop()
