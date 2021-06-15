'''
The CropRatio can be used to calculate what proportion of a farm's harvest is a specific crop.

For Example:
    crop_ratio = CropRatio(['Wheat', 'Rice'])
    crop_ratio.add('Wheat', 4)
    crop_ratio.add('Wheat', 5)
    crop_ratio.add('Rice', 1)
Should return 0.9
'''
class CropRatio:
    def __init__(self):
        self.crops = {}
        self.total_weight = 0

    def add(self, name, crop_weight):
        if name not in self.crops:
            self.crops[name] = 0
        self.crops[name] += crop_weight 
        self.total_weight += crop_weight

    def proportion(self, name):
        if name not in self.crops:
            return None
        if self.crops == None:
            self.total_weight = 0
            return None
        else:
            return self.crops[name]/self.total_weight

if __name__ == "__main__":

    crop_ratio = CropRatio()
    crop_ratio.add('Wheat', 4)
    crop_ratio.add('Wheat', 5)
    crop_ratio.add('Rice', 1)
    
    print(crop_ratio.proportion('Wheat'))



