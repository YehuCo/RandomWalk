from random import choice, randint

class RandomWalk:
    """Class to generate random walks"""

    def __init__(self, numPoints=50_000):
        """Initialize attributes of a walk"""
        self.numPoints = numPoints

        # all walks start at (0, 0)
        firstX = randint(0, self.numPoints)
        firstY = randint(0, self.numPoints)
        self.xValues = [0]
        self.yValues = [0]

    def FillWalk(self):
        """Fill the walk with points"""

        while len(self.xValues) < self.numPoints:
            # get x and y steps
            xStep = self.GetStep()
            yStep = self.GetStep()

            # ignore moves that go nowhere
            if xStep == 0 and yStep == 0:
                continue

            # calculate new position
            x = self.xValues[-1] + xStep
            y = self.yValues[-1] + yStep
            self.xValues.append(x)
            self.yValues.append(y)

    def GetStep(self):
        """Calculate points in the walk"""

        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step
