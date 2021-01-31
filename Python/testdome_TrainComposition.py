""""
A TrainComposition is built by attaching and detaching wagons from the left and the right sides, efficiently with respect to time used.

For example, if we start by attaching wagon 7 from the left followed by attaching wagon 13, again from the left, we get a composition of two wagons (13 and 7 from left to right). Now the first wagon that can be detached from the right is 7 and the first that can be detached from the left is 13.

Implement a TrainComposition that models this problem.
"""
import collections


class TrainComposition:

    def __init__(self):
        self.train = collections.deque()

    def attach_wagon_from_left(self, wagonId):
        self.train.appendleft(wagonId)

    def attach_wagon_from_right(self, wagonId):
        self.train.append(wagonId)

    def detach_wagon_from_left(self):
        return self.train.popleft()

    def detach_wagon_from_right(self):
        return self.train.pop()


if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right())  # should print 7
    print(train.detach_wagon_from_left())  # should print 13