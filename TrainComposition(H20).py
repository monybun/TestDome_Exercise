'''
A TrainComposition is built by attaching and detaching wagons from the left and the right sides,
efficiently with respect to time used.

For example, if we start by attaching wagon 7 from the left followed by attaching wagon 13,
again from the left, we get a composition of two wagons (13 and 7 from left to right).

Now the first wagon that can be detached from the right is 7 and the first that can be detached from the left is 13.

Implement a TrainComposition that models this problem.

'''

'''
##colloction-->deque :	list-like container with fast appends and pops on either end

import collections

class TrainComposition:
    
    def __init__(self):

        self.train = collections.deque()
    
    def attach_wagon_from_left(self, wagonId):

        self.train.appendleft(wagonId)
    
    def attach_wagon_from_right(self, wagonId):

        self.train.append(wagonId)

    def detach_wagon_from_left(self):

        return self.train.popleft() if self.train else None
    
    def detach_wagon_from_right(self):

        return self.train.pop() if self.train else None

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13

'''

## METHOD TWO : using dictionary
class TrainComposition:

    def __init__(self):
        self.train = dict()
        self.left  = 1
        self.right = 0

    def attach_wagon_from_left(self, wagonId):
        
        self.left -= 1
        self.train[self.left] = wagonId

    def attach_wagon_from_right(self, wagonId):
        
        self.right += 1
        self.train[self.right] = wagonId

    def detach_wagon_from_left(self):
        
        if self.left > self.right:
            return None
        
        wagonId = self.train[self.left]
        del self.train[self.left]
        self.left += 1
        return wagonId

    def detach_wagon_from_right(self):
        
        if self.left>self.right:
            return None
        
        wagonId = self.train[self.right]
        del self.train[self.right]
        self.right -= 1
        return wagonId
    
if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13


