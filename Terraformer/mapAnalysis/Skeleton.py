import numpy as np
import skan
from skimage.morphology import skeletonize
from skan.csr import skeleton_to_csgraph
from collections import Counter

from gdpc import Block as place

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
        print(coordinates)
        for i in range(len(coordinates)):
            coordinates[i] = list(coordinates[i])

        print(coordinates)
        coordinates_final = []
        print(len(coordinates[0]))
        print((coordinates[0]))
        print(len(coordinates[1]))
        print((coordinates[1]))
        print(len(coordinates[2]))
        print((coordinates[2]))
        for i in range(len(coordinates[0])):
            print((coordinates[2][i], coordinates[1][i], coordinates[0][i]))
            coordinates_final.append((coordinates[2][i], coordinates[1][i], coordinates[0][i]))

        self.coordinates = coordinates_final

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


### Visualisation ###


from PIL import Image
from gdpc import Editor
import random

def heightmap(
    mapName="heightmap.png",
    biomeName="heightmap_biome.png",
):
    """
    Generate a heightmap using nbt data.

    Args:
        xzStart (tuple): xz coordinates of the northwest corner of the
        area to scan.
        xzDistance (tuple): xz distance of the southwest corner from the
        northwest corner.

    Returns:
        heightmap.png

    >>> heightmap((-256, -256), (512, 512))
    """

    editor = Editor()

    buildArea = editor.getBuildArea()
    buildRect = buildArea.toRect()
    xzStart = buildRect.begin
    xzDistance = (max(buildRect.end[0], buildRect.begin[0]) - min(buildRect.end[0], buildRect.begin[0]), max(buildRect.end[1], buildRect.begin[1]) - min(buildRect.end[1], buildRect.begin[1]))

    heightmap = Image.new(
        "RGBA",
        (xzDistance[0], xzDistance[1]),
        "red",
    )

    # heightmapBiome = Image.new(
    #     "RGBA",
    #     (xzDistance[0], xzDistance[1]),
    #     "red",
    # )

    slice = editor.loadWorldSlice(buildRect)
    heightmapData = list(
        np.array(slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"], dtype=np.uint8)
    )

    for x in range(0, xzDistance[0]):
        for z in range(0, xzDistance[1]):
            y = heightmapData[x][z]
            biomeId = slice.getBiome((xzStart[0] + x, 0, xzStart[1] + z))
            block = slice.getBlock((xzStart[0] + x, y, xzStart[1] + z))
            #heightmapBiome.putpixel((x, z), heightmapColor(y, biomeId, block))
            heightmap.putpixel((x, z), (y, y, y))

    heightmap.save(mapName)
    #heightmapBiome.save(biomeName)

def skeletonVisualisation(skeleton): # not working due to indicies
    editor = Editor()

    buildArea = editor.getBuildArea()
    buildRect = buildArea.toRect()
    xzStart = buildRect.begin
    xzDistance = (max(buildRect.end[0], buildRect.begin[0]) - min(buildRect.end[0], buildRect.begin[0]), max(buildRect.end[1], buildRect.begin[1]) - min(buildRect.end[1], buildRect.begin[1]))
    
    path = "heightmap.png"
    # Lines
    im = Image.open("heightmap.png")
    print(im.size)
    width, height = im.size
    # img = Image.new(mode="RGB", size=(width, height))

    for i in range(len(skeleton.lines)):
        r, g, b = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        for j in range(len(skeleton.lines[i])):
            print(skeleton.lines[i])
            print(j, "j", skeleton.lines[i][j], "h")
            z = skeleton.coordinates[skeleton.lines[i][j]][0]
            y = skeleton.coordinates[skeleton.lines[i][j]][1]
            x = skeleton.coordinates[skeleton.lines[i][j]][2]
            # editor.placeBlock((x, y, z), place("minecraft:white_concrete"))
            im.putpixel(
                (
                    int(skeleton.coordinates[skeleton.lines[i][j]][2])-1,
                    int(skeleton.coordinates[skeleton.lines[i][j]][0])-1,
                ),
                (r + j, g + j, b + j),
            )
    im.save(path, "PNG")

    # Centers
    for i in range(len(skeleton.centers)):
        print(skeleton.coordinates[skeleton.centers[i]])
        im.putpixel(
            (int(skeleton.coordinates[skeleton.centers[i]][0]), int(skeleton.coordinates[skeleton.centers[i]][1])),
            (255, 255, 0),
        )
    im.save(path, "PNG")

    # Intersections
    for i in range(len(skeleton.intersections)):
        intersection = []
        for j in range(len(skeleton.intersections[i])):
            intersection.append(skeleton.coordinates[skeleton.intersections[i][j]])

        for i in range(len(intersection)):
            im.putpixel(
                (int(skeleton.intersections[i][0]), int(skeleton.intersections[i][1])),
                (255, 0, 255),
            )
    im.save(path, "PNG")