import torch
import numpy as np
from PIL import Image
from Training import ImageNormalizer
import Model1

DEFAULT_MODEL_PATH = r'C:\Users\endpl\Desktop\GHP\Trainerds\models\TrainedModel1.pth'

# Set up devices for possible GPU accelleration
CURRENT_DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
CPU_DEVICE = torch.device("cpu")

def generateTerrain(inputImage: Image, loadedModelPath = "default") -> Image:
    # Set default path
    if (loadedModelPath == "default"):
        loadedModelPath = DEFAULT_MODEL_PATH

    # Initialize ML Model
    ml = Model1.MainModel()
    ml.loadModelFromPath(loadedModelPath)
    
    # Set up Tensors
    trainingTensor = ImageNormalizer.imageToTensor(input).to(CURRENT_DEVICE)

    # Forward Pass
    outputTensor = ml(trainingTensor)

    # Return outputImage
    outImage = outputToImage(outputTensor)
    return outImage

#Path = r"C:\Users\endpl\Desktop\GHP\Trainerds\Training\Unsized Training Images\heightmap.png"

# Normalize data
def outputToImage(output: torch.Tensor) -> Image:
    outputTensor = output - output.min()  # Shift the tensor so the minimum value is 0
    outputTensor = outputTensor / outputTensor.max()  # Normalize to the range [0, 1]
    outputTensor.to(CPU_DEVICE)

    # Apply threshold to round values to 0 or 1 and make image fully black/white
    threshold = 0.5
    outputTensor = torch.where(outputTensor < threshold, torch.tensor(0.0), torch.tensor(1.0))
    outputTensor = outputTensor * 255 # Set white pixels to be full white 

    array = outputTensor.detach().numpy().astype(np.uint8) # Tensor to array
    image = Image.fromarray(array, mode='L')  # 'L' mode is for (8-bit pixels, black and white)
    return image

def printParams(model) -> None:
    # Print each of the model's tensor parameters
    for name, param in model.named_parameters():
                print(f"{name}: {param}")