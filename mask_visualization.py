import sys
import numpy as np
import matplotlib.pyplot as plt

# Get the image path from the command-line arguments
if len(sys.argv) < 2:
    print('Usage: python visualize_image.py <image_file>')
    sys.exit()
image_path = sys.argv[1]

# Load the image from the specified file
try:
    image = np.load(image_path)
except:
    print('Error: could not load image from file "{}"'.format(image_path))
    sys.exit()

image = image.astype(np.float32)

print(image.shape)

# Display the image using matplotlib
plt.imshow(image, cmap='gray')
plt.scatter([205.75502, 366.00232, 401.61282, 265.10587], [344.07187, 391.55255, 350.99612, 309.45053])
plt.axis('off')
plt.show()
