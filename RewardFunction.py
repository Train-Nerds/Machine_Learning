from PIL import Image
import PathAlgorithm



class Reward_Function():
    inputImage = None
    outputRailImage = None
    rewardModifier = None
    waterLevel = None
    cityColor = None
    imageWidth = 1000
    imageHeight = 1000

    def __init__():
        pass
    def __init__(rewardModifier: float, waterLevel: int, cityColor: int):
        self.cityColor = cityColor
        self.waterLevel = waterLevel
        self.rewardModifier = rewardModifier    

    def Calculate(self):
        inputImage = None
        outputRailImage = None        
        reward = self.reward_Calculator()
        pass

    def cost_Calculator(self):
        self.inputImage
        self.outputRailImage
        cost = 0
        for pixil_Index in range(len(self.inputImage)):
            if(self.outputRailImage[pixil_Index] != (0,0,0)):
                cost += pixil_Cost_Calculator(pixil_Index)
        return(cost)
    def pixil_Cost_Calculator(pixil_Index: int):
        terrain_Pixil_Value = self.inputImage[pixil_Index]
        if(terrain_Pixil_Value > self.waterLevel):
            return(2*terrain_Pixil_Value[0])
        else:
            return(terrain_Pixil_Value[0]*terrain_Pixil_Value[0])


    def value_Calculator(self):

        pass
    def efficiency_Calculator(self):
        trainMap_As_Binary = []
        for pixil in self.inputImage:
            if(pixil[0] < 10):
                trainMap_As_Binary += [0]
            else:
                trainMap_As_Binary += [1]
        grid = [trainMap_As_Binary[row:row + self.imageWidth] for row in range(self.imageHeight-1)]
           
        


        PathAlgorithm.a_star_search()
        pass

    def reward_Calculator(inputImage: Image, outputRailImage: Image):
        self.inputImage = list(inputImage.getdata())
        self.outputRailImage = list(outputRailImage.getdata())

        cost = cost_Calculator()
        value = value_Calculator()
        efficiency = efficiency_Calculator()
        reward = None

        cost_Calculator()


