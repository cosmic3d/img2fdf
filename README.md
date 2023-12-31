# img2fdf

## What is img2fdf?

`img2fdf` is a Python program that converts an image into a .fdf map file, which you can run in the [FilDeFer](https://github.com/cosmic3d/ft_fdf) 42 campus project. Each pixel of the image is represented as a point in the map, with its corresponding color assigned in hexadecimal format. The resulting .fdf map can be used in various applications that require color mapping.

## How to Use

1. Install the necessary requirements (see the Requirements section).
2. Run the `img2fdf.py` script, providing the path to the image as input.
3. The program will generate the corresponding .fdf map file in the `output` folder.

```shell
python3 img2fdf.py
```

## Requirements

- Python 3.6 or above
- PIL (Python Imaging Library) package

Run this command on the project folder to install all the requirements:
```shell
pip3 install -r requirements.txt
```
