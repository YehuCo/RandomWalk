from ctypes import pointer
import matplotlib.pyplot as plt
from RandomWalk_Class import *

# keep generating new walks until program is killed
while True:
    # make a random walk
    rw = RandomWalk(500_000)
    rw.FillWalk()

    # plot the points from the walk
    plt.style.use('seaborn-dark')
    fig, ax = plt.subplots(figsize=(9, 7))
    pointNumbers = range(rw.numPoints)
    ax.scatter(rw.xValues, rw.yValues, c=pointNumbers, cmap=plt.cm.Greens, edgecolors='none', s=3)

    # emphasize first and last points
    ax.scatter(rw.xValues[0], rw.yValues[0], c='green', edgecolors='none', s=100)
    ax.scatter(rw.xValues[-1], rw.yValues[-1], c='red', edgecolors='none', s=100)

    # plot title
    ax.set_title("Random Walk", fontsize=20)

    plt.show()

    keepRunning = input("Generate another walk? (y/n) " )
    if keepRunning == 'n':
        break
