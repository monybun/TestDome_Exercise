"""
The following RewardPoints class tracks how many reward points every customer has earned. 
Enhance the class so that it satisfies the following conditions:

When a customer earns points for the first time (more than 0), they receive an additional 500 bonus points. 

spend_points should always return the number of points a customer has earned. 
If the customer is unknown, 0 points should be returned. 
If 0 or less points is passed to earn_points or spend_points, a customer's points should be unaffected.
If more points are passed to spend_points than the customer has available then their current balance should be returned unaffected.

For example:

rewardPoints = RewardPoints()
rewardPoints.earn_points('John', 520)
print(rewardPoints.spend_points('John', 200))

Should display: 820
"""
from collections import defaultdict

class RewardPoints:
    def __init__(self):
        self.customers = defaultdict(int)
        
    def earn_points(self, customer_name, points):
        
        earned_points = 0
        self.customers[customer_name] = points
        self.customers[customer_name] += points
        
        if customer_name not in self.customers:
            earned_points = 0
        elif customer_name in self.customers and self.customers[customer_name] == 0:
            earned_points = 500 + points
        else:
            earned_points = self.customers[customer_name]
        return earned_points
    
    def spend_points(self, customer_name, points):
        if points <= 0 or points > self.customers[customer_name] : pass
        
        for customer_name in self.customers.keys():
            self.customers[customer_name] -= points
        
        return self.customers[customer_name]
        
if __name__ == "__main__":
    rewardPoints = RewardPoints()
    rewardPoints.earn_points('John', 520)
    print(rewardPoints.spend_points('John', 200))
