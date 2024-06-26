import torch
from PIL import Image
import numpy as np

def imageToTensor(image_path) -> torch.Tensor:
    # Open the image file
    img = Image.open(image_path)
    
    # Check if the image size is 1000x1000
    if img.size!= (1000, 1000):
        raise ValueError("Image dimensions must be 1000x1000.")
    
    # Convert the image data to numpy arrays
    rgbData = np.array(img.convert('RGB'))
    
    normalizedRgbData = rgbData[:, :, :] / 255.0

    rgbTensor = torch.from_numpy(normalizedRgbData).float()
    
    return rgbTensor