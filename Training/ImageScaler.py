from PIL import Image

def scaleImage(inName,outName,sqSize=1000,save=False) -> Image:
    # Scale PNG image to 1000x1000 (or other square size) from any given size, returns Image object and can save the image
    image = Image.open(f'C:\\Users\\endpl\\Desktop\\GHP\\Trainerds\\Training\\Unsized Training Images\\{inName}.png')
    newImage = image.resize((sqSize,sqSize), resample=Image.BOX)
    if (save):
        newImage.save(f'C:\\Users\\endpl\\Desktop\\GHP\\Trainerds\\Training\\Sized Training Images\\{outName}.png')
    return newImage
