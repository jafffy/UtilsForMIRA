# PNG to NumPy Converter

This Python script converts a PNG image to a NumPy array and saves it to a .npy file. It can be run from the command line and takes an input file path as a required argument and an optional output file path argument. If the output file path is not specified, the script replaces the input file extension with .npy and uses that as the output file path.

## Requirements

This script requires the following Python packages:

- Pillow (PIL fork)
- NumPy

You can install these packages using pip:

```sh
pip install pillow numpy
```

## Usage

```sh
python png_to_npy.py INPUT_FILE [-o OUTPUT_FILE]
```

- `INPUT_FILE` (required): the input PNG file path
- `-o, --output (optional): the output .npy file path
- 
If the `-o` or `--output` option is not used, the script saves the output file with the same name as the input file, but with the .npy extension.

Convert `image.png` to `image.npy`:

```sh
python png_to_npy.py image.png
```

Convert `image.png` to `data.npy`:

```sh
python png_to_npy.py image.png -o data.npy
```

## License

This script is released under the MIT License.