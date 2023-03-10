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
meshRotateAngle = np.array(mat_data['meshRotateAngle'], dtype=np.float32)
meshRotateAxis = np.array(mat_data['meshRotateAxis'], dtype=np.float32)
meshScale = np.array(mat_data['meshScale'], dtype=np.float32)
meshTranslate = np.array(mat_data['meshTranslate'], dtype=np.float32)

# Save NumPy ndarrays to .npz file
np.savez(args.output_file, meshRotateAngle=meshRotateAngle, meshRotateAxis=meshRotateAxis,
         meshScale=meshScale, meshTranslate=meshTranslate)

print(f'Successfully converted {args.input_file} to {args.output_file}')
