import argparse
import numpy as np
from PIL import Image


def npy_to_png(input_file, output_file):
    # load the numpy array from the input file
    array = np.load(input_file)

    # normalize the array values to the range [0, 255]
    array = (array - np.min(array)) / (np.max(array) - np.min(array)) * 255

    # convert the array to an image
    image = Image.fromarray(array.astype('uint8'))

    # save the image as a PNG file
    image.save(output_file)


if __name__ == '__main__':
    # parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert a NumPy array in a .npy file to a PNG image')
    parser.add_argument('input_file', help='the input .npy file')
    parser.add_argument('-o', '--output', help='the output PNG file')
    args = parser.parse_args()

    # set default output file name if not provided
    if args.output is None:
        args.output = args.input_file.replace('.npy', '.png')

    # call npy_to_png function with input and output file names
    npy_to_png(args.input_file, args.output)
