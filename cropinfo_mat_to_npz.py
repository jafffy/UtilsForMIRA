import scipy.io
import numpy as np
import argparse

# Set up argparse to allow user to specify input and output file paths
parser = argparse.ArgumentParser(description='Convert MATLAB .mat file to NumPy .npz file')
parser.add_argument('input_file', type=str, help='Path to input .mat file')
parser.add_argument('output_file', type=str, help='Path to output .npz file')
args = parser.parse_args()

# Load data from .mat file
mat_data = scipy.io.loadmat(args.input_file)

# Convert loaded data to NumPy ndarrays
xMask = np.array(mat_data['xMask'], dtype=np.float32)
yMask = np.array(mat_data['yMask'], dtype=np.float32)
xObj = np.array(mat_data['xObj'], dtype=np.float32)
yObj = np.array(mat_data['yObj'], dtype=np.float32)

print(xMask.shape, yMask.shape, xObj.shape, yObj.shape)

# Save NumPy ndarrays to .npz file
np.savez(args.output_file, xMask=xMask, yMask=yMask, xObj=xObj, yObj=yObj)

print(f'Successfully converted {args.input_file} to {args.output_file}')
