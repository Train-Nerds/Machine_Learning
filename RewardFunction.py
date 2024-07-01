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
    cityCoords = []

    def __init__(self, rewardModifier: float, waterLevel: int, cityColor: int):
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
                cost += self.pixil_Cost_Calculator(pixil_Index)
        return(cost)
    def pixil_Cost_Calculator(self, pixil_Index: int):
        terrain_Pixil_Value = self.inputImage[pixil_Index]
        if(terrain_Pixil_Value > self.waterLevel):
            return(2*terrain_Pixil_Value[0])
        else:
            return(terrain_Pixil_Value[0]*terrain_Pixil_Value[0])



    def findCityLocations(self):
        for pixil_Index in range(len(self.inputImage)-1):
            pixil = self.inputImage[pixil_Index]
            pixilGrid = [[pixil[y*self.imageWidth+x] for x in range(self.imageWidth-1)] for y in range(self.imageHeight-1)]
            for y in range(len(pixilGrid)-1):
                for x in range(len(pixilGrid[y])-1):
                    if(pixilGrid[y][x] == self.cityColor):
                        print(str(x) + ' ' + str(y) + ' ' + str(pixilGrid[y][x]))
                        self.cityCoords.append([x, y])

    def efficiency_Value_Calculator(self):
        trainMap_As_Binary = []
        for pixil in self.outputRailImage:
            if(pixil[0] < 10):
                trainMap_As_Binary += [0]
            else:
                trainMap_As_Binary += [1]
        grid = [[trainMap_As_Binary[y*self.imageWidth+x] for x in range(self.imageWidth-1)] for y in range(self.imageHeight-1)]
        
        value = 0
        efficiency = 0
        for cityCoord in self.cityCoords:
            for connectedCityCoord in self.cityCoords:
                pathLength = PathAlgorithm.a_star_search(grid=grid, src=cityCoord, dest=connectedCityCoord)
                if(pathLength >= 0):
                    value += 1
                    efficiency -= pathLength
        return(value, efficiency)

    def reward_Calculator(self, inputImage: Image, outputRailImage: Image, ):
        self.inputImage = list(inputImage.getdata())
        self.outputRailImage = list(outputRailImage.getdata())
        self.findCityLocations()

        cost = self.cost_Calculator()
        value, efficiency = self.efficiency_Calculator()
        reward = pow(self.rewardModifier, value)/efficiency-cost
        return(reward)


