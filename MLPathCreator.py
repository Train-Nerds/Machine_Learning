import torch
import numpy as np
from PIL import Image
import Model1

# Changed to have ImageNormalizer functions within file

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
    trainingTensor = imageToTensor(inputImage).to(CURRENT_DEVICE)

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

def imageToTensor(img) -> torch.Tensor:
    # Convert a 1000x1000 image's R, G, and B channels into a float tensor with values between 0 and 1

    # Check if the image size is 1000x1000
    if img.size!= (1000, 1000):
        raise ValueError("Image dimensions must be 1000x1000.")
    
    # Convert the image data to numpy arrays
    rgbData = np.array(img.convert('RGB'))
    
    # Normalize values bteween 0 and 1 for better training accuracy
    normalizedRgbData = rgbData[:, :, :] / 255.0

    rgbTensor = torch.from_numpy(normalizedRgbData).float().permute(2,0,1) # Permute to convert to Channel, height, width format for AI
    
    return rgbTensor

def railImageToTensor(img) -> torch.Tensor:
    # Convert a 1000x1000 image's R, G, and B channels into a float tensor with values between 0 and 1

    # Check if the image size is 1000x1000
    if img.size!= (1000, 1000):
        raise ValueError("Image dimensions must be 1000x1000.")
    
    # Convert the image data to numpy arrays
    grayData = np.array(img.convert('L'))
    
    # Normalize values bteween 0 and 1 for better training accuracy
    normalizedGrayData = grayData[:, :] / 255.0

    grayTensor = torch.from_numpy(normalizedGrayData).float().permute(0,1) # Permute to convert height, width
    
    return grayTensor

def imageToTensorFromPath(imagePath) -> torch.Tensor:
    # Run imageToTensor with a specified path
    
    # Open the image file
    img = Image.open(imagePath)
    
    rgbTensor = imageToTensor(img)
    
    return rgbTensor
