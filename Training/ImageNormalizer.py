import torch
from PIL import Image
import numpy as np

def imageTensors(image_path):
    img = Image.open(image_path)
    
    # Check if the image size is 1000x1000
    if img.size!= (1000, 1000):
        raise ValueError("Image dimensions must be 1000x1000.")
    
    # Convert the image data to numpy arrays
    rgba_data = np.array(img.convert('RGBA'))
    
    # Separate the RGBA channels
    rChannel = rgba_data[:, :, 0]
    gChannel = rgba_data[:, :, 1]
    bChannel = rgba_data[:, :, 2]
    #aChannel = rgba_data[:, :, 3]

    rNormal = rChannel / 255.0
    gNormal = gChannel / 255.0
    bNormal = bChannel / 255.0
    
    # Convert the numpy arrays to PyTorch tensors
    rTensor = torch.from_numpy(rNormal).float()
    gTensor = torch.from_numpy(gNormal).float()
    bTensor = torch.from_numpy(bNormal).float()
    
    return rTensor, gTensor, bTensor
