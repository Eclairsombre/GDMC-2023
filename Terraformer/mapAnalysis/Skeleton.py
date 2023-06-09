import numpy as np
import skan
from skimage.morphology import skeletonize
from skan.csr import skeleton_to_csgraph
from collections import Counter

data = np.array([[[False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True]], [[False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True]], [[False, False, False, False, False, True, True, True, True, True, True, True, False], [False, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True]], [[False, False, False, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, False, False, False]], [[False, False, False, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, False, False, False, False]], [[False, False, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, False, False, False, False, False, False]], [[False, False, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, False, False, False, False], [True, True, True, True, True, False, False, False, False, False, False, False, False]], [[False, False, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, False, False, False, False, False, False, False], [True, True, True, True, False, False, False, False, False, False, False, False, False]], [[False, False, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, False, False, True, True, True], [True, True, True, True, True, False, False, False, False, False, False, False, False], [True, True, True, False, False, False, False, False, False, False, False, False, False]], [[False, False, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, False, False, False, False, False], [True, True, True, True, True, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False]], [[False, False, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, False, False, False, False, False], [True, True, True, True, True, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False]], [[False, False, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, False, False, False], [True, True, True, True, True, True, True, True, False, False, False, False, False], [True, True, True, True, True, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False]]])

class Skeleton:
    def __init__(self):
        self.lines = []
        self.intersections = []
        self.centers = []
        self.graph = []
        self.coordinates = []

    def setSkeleton(self, data):

        binary_skeleton = skeletonize(data)

        graph, coordinates = skeleton_to_csgraph(binary_skeleton)
        self.graph = graph.tocoo()

        # List of lists. Inverted coordinates.
        coordinates = list(coordinates)
        for i in range(len(coordinates)):
            coordinates[i] = (coordinates[i][1], coordinates[i][0])

        self.coordinates = coordinates

    def findNextElements(self, key):
        """Find the very nearest elements"""

        line = []

        values = np.array(self.graph.row)
        indices = np.where(values == key)[0]

        for i in range(len(indices)):
            if self.graph.row[indices[i]] == key:
                line.append(self.graph.col[indices[i]])
        return line

    def findLine(self, key):
        nextKeys = self.findNextElements(key)

        if len(nextKeys) >= 3:  # Intersections.
            return nextKeys

        if len(nextKeys) == 2 or len(nextKeys) == 1:  # In line or endpoints.
            line = []
            line.append(key)
            line.insert(0, nextKeys[0])
            if len(nextKeys) == 2:
                line.insert(len(line), nextKeys[1])

            nextKeys = line[0], line[-1]

            while len(nextKeys) == 2 or len(nextKeys) == 1:
                extremity = []
                for key in nextKeys:
                    nextKeys = self.findNextElements(key)

                    if len(nextKeys) <= 2:
                        # Add the neighbors that is not already in the line.
                        for element in nextKeys:
                            if element not in line:
                                extremity.append(element)
                                line.append(element)

                    if len(nextKeys) >= 3:
                        # Add the intersection only.
                        extremity.append(key)

                    nextKeys = []
                    for key in extremity:
                        ends = self.findNextElements(key)
                        if len(ends) == 2:
                            nextKeys.append(key)
            return line

    def parseGraph(self):
        for key, value in sorted(
            Counter(self.graph.row).items(), key=lambda kv: kv[1], reverse=True
        ):
            print(value, "hey 3")
            # Start from the biggest intersections.
            if value != 2:  # We don't want to be in the middle of a line.
                line = self.findLine(key)

                # We have now all the connected points if it's an
                # intersection. We need to find the line.

                if value != 1:
                    # It's not an endpoint.
                    self.centers.append(key)
                    self.intersections.append(line)
                    for i in line:
                        line = self.findLine(i)

                        if i in line:
                            # The key is inside the result : it's a line.
                            alreadyInside = False
                            for l in self.lines:
                                # Verification if not already inside.
                                if Counter(l) == Counter(line):
                                    alreadyInside = True
                                    # print(line, "inside", lines)

                            if alreadyInside == False:
                                self.lines.append(line)
                                print(line, "hey 2")
                        else:
                            # The key is not inside the result, it's an
                            # intersection directly connected to the key.
                            line = [key, i]
                            alreadyInside = False
                            for l in self.lines:
                                # Verification if not already inside.
                                if Counter(l) == Counter(line):
                                    alreadyInside = True
                                    # print(line, "inside", lines)

                            if alreadyInside == False:
                                self.lines.append(line)
                                print(line, "hey 1")


from skimage.data import binary_blobs
blobs = binary_blobs(16, volume_fraction=0.3, n_dim=3)

# # # # # #
import sys
sys.path.append("Terraformer/dataAcquisition/")
import World

w = World.World()

import sys
sys.setrecursionlimit(w.length_x * w.length_y * w.length_z)

w.propagate((2158, 125, 560))
print("done")
print(w.binaryImage())

# # # # # #

# print(blobs)
# print("-----------------------------------------")
# print(data, "date")

skel = Skeleton()

skel.setSkeleton(w.binaryImage())

skel.parseGraph()
print(skel.centers)
print(skel.lines)
print(skel.intersections)