import torch
import numpy as np
from PIL import Image
import Model1
from Training import ImageScaler
from Training import ImageNormalizer
import RewardAlgorithm

#Path = r"C:\Users\endpl\Desktop\GHP\Trainerds\Training\Unsized Training Images\heightmap.png"
imgName = "heightmap"
scaledImage = ImageScaler.scaleImage(imgName,"sized1",save=True)
print(scaledImage)
traningTensor = ImageNormalizer.imageToTensor(scaledImage)
print(traningTensor.shape)
ml = Model1.MainModel()
outputTensor = ml(traningTensor)
print(f"Output tensor shape: {outputTensor.shape}")

# Normalize data
outputTensor = outputTensor - outputTensor.min()  # Shift the tensor so the minimum value is 0
outputTensor = outputTensor / outputTensor.max()  # Normalize to the range [0, 1]

# Apply threshold to round values to 0 or 1 and make image fully black/white
threshold = 0.5
outputTensor = torch.where(outputTensor < threshold, torch.tensor(1.0), torch.tensor(0.0))

outputTensor = outputTensor * 255
array = outputTensor.detach().numpy().astype(np.uint8)
image = Image.fromarray(array, mode='L')  # 'L' mode is for (8-bit pixels, black and white)
image.save(f'Trainerds\\Training\\Completed Images\\finished1.png')

print(f"Final Reward:{RewardAlgorithm.calcReward(scaledImage,image)}")