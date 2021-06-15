'''
Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping.
If there are no ingredients or toppings, the method should return an empty list.

For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()
should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
'''

class IceCreamMachine:
    
    all={}
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        re = []
        for i in self.ingredients:
            for j in self.toppings:
                re.append([i, j])
        return re

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())
