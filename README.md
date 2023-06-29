# img2fdf

## What is img2fdf?

`img2fdf` is a Python program that converts an image into a .fdf map file. Each pixel of the image is represented as a point in the map, with its corresponding color assigned in hexadecimal format. The resulting .fdf map can be used in various applications that require color mapping.

## How to Use

1. Install the necessary requirements (see the Requirements section).
2. Run the `img2fdf.py` script, providing the path to the image as input.
3. The program will generate the corresponding .fdf map file in the `output` folder.

```shell
$ python3 img2fdf.py path/to/image.png
