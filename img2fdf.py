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
            color_hex = "0x{:02X}{:02X}{:02X}".format(r, g, b)
            fdf_map += "0,{} ".format(color_hex)

        fdf_map += "\n"

    return fdf_map.strip()

def save_fdf_file(image_path, fdf_content):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, "output")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_name = os.path.splitext(os.path.basename(image_path))[0]
    output_file = os.path.join(output_folder, "{}.fdf".format(file_name))

    with open(output_file, "w") as f:
        f.write(fdf_content)

# Ejemplo de uso
while True:
    input_image = input("Path to the image with file extension (or 'exit' to quit): ")
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
