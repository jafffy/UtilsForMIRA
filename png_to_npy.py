import argparse
import os
from PIL import Image
import numpy as np

# Define the command line interface
parser = argparse.ArgumentParser(description='Convert a PNG image to a NumPy array and save it to a .npy file')
parser.add_argument('input', metavar='INPUT_FILE', help='the input PNG file')
parser.add_argument('-o', '--output', metavar='OUTPUT_FILE', help='the output .npy file')

# Parse the command line arguments
args = parser.parse_args()

# Load the image
img = Image.open(args.input)

# Convert the image to a NumPy array
img_arr = np.array(img)

# Determine the output file path
if args.output:
    output_path = args.output
else:
    # Replace the input file extension with .npy
    output_path = os.path.splitext(args.input)[0] + '.npy'

# Save the NumPy array as a .npy file
np.save(output_path, img_arr)
