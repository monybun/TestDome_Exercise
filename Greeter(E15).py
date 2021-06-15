"""
The greeter greets people entering a hotel. The boss should be greeted with 'Hello, {name}', 
while everyone else should be greeted with 'Welcome, {name}'. If multiple people enter, 
only the person who entered last should be greeted. If no one has entered since the last greeting, 
a call to greet() should return None.

For example, the following code should display 'Welcome, John':
g = Greeter('Chuck')
g.enters('John')
print(g.greet())
"""
class Greeter:

    def __init__(self, boss):
        self.boss = boss
        print('Hello, {}'.format(self.boss))
        
    def enters(self, visitor):
        
        if type(visitor) == list:
            self.visitor = []
            for i in visitor:
                self.visitors.append(i)
            self.visitor = self.visitor[-1]

        else:
            self.visitor = visitor
        
        return self.visitor
    
    def greet(self):
        if self.visitor == self.boss:
            return 'Hello, {}'.format(self.boss)
        else:
            return'Welcome, {}'.format(self.visitor)
        
if __name__ == "__main__":
    g = Greeter('Chuck')
    g.enters('John')
    print(g.greet())