from PIL import Image
import os

def generate_fdf_map(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    width, height = img.size

    fdf_map = ""
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            color_hex = f"0x{r:02X}{g:02X}{b:02X}"
            fdf_map += f"0,{color_hex} "

        fdf_map += "\n"

    return fdf_map.strip()

def save_fdf_file(image_path, fdf_content):
    base_path = os.path.dirname(image_path)
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    output_folder = os.path.join(base_path, "output")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, f"{file_name}.fdf")

    with open(output_file, "w") as f:
        f.write(fdf_content)

# Ejemplo de uso
while True:
    input_image = input("Path to the image (or 'exit' to quit): ")
    if input_image.lower() == "exit":
        break

    try:
        output_fdf = generate_fdf_map(input_image)
        save_fdf_file(input_image, output_fdf)
        print("Conversion completed successfully.")
        break
    except FileNotFoundError:
        print("File not found. Please provide a valid image file.")
    except Exception as e:
        print("Error:", e)
        break
