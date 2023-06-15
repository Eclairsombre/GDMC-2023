import numpy as np
import maths
import math

import main
# from gdpc import Block as place
# import Editor

import random
from random import randint

from PIL import Image
from collections import Counter

alreadyGenerated = []

import sys
sys.path.append("Generator/Constructions/houses")
import house


######################## Lanes materials presets #######################


standard_modern_lane_composition = {
    "road_surface": {
        "black_concrete": 3,
        "coal_block": 1,
        "black_concrete_powder": 2,
    },
    "median_strip": {"stone": 1},
    "structure": {"stone": 3, "andesite": 1},
    "central_lines": {"yellow_concrete": 3, "yellow_concrete_powder": 1},
    "external_lines": {"white_concrete": 3, "white_concrete_powder": 1},
    "lines": {"white_concrete": 3, "white_concrete_powder": 1},
}

# editor.placeBlock((x, y, z), place("minecraft:white_concrete"))

######################### Additional functions #########################


def cleanLanes(lanes):
    cleanLanes = {}
    for lane in lanes:
        for xyz in lanes[lane]:
            if (round(xyz[0]), round(xyz[1]), round(xyz[2]),) not in [
                cleanLanes[i][j]
                for __, i in enumerate(cleanLanes)
                for j in range(len(cleanLanes[i]))
            ]:
                if cleanLanes.get(lane) == None:
                    cleanLanes[lane] = []
                cleanLanes[lane].append(
                    (round(xyz[0]), round(xyz[1]), round(xyz[2]))
                )
    return cleanLanes


############################ Lanes functions ###########################

housesCoordinates = []


def singleLaneLeft(XYZ, blocks=standard_modern_lane_composition):
    """Left side."""

    factor = 8
    distance = 2

    roadMarkings = maths.curveSurface(
        np.array(XYZ),
        distance + 1,
        resolution=0,
        pixelPerfect=True,
        factor=1,
        start=2,
    )
    roadMarkings = cleanLanes(roadMarkings)

    roadSurface = maths.curveSurface(
        np.array(XYZ),
        distance,
        resolution=0,
        pixelPerfect=False,
        factor=factor,
    )
    roadSurface = cleanLanes(roadSurface)

    walkway = maths.curveSurface(
        np.array(XYZ),
        distance + 3,
        resolution=0,
        pixelPerfect=False,
        factor=4,
        start=3,
    )
    walkway = cleanLanes(walkway)

    houses = maths.curveSurface(
        np.array(XYZ),
        distance + 14,
        resolution=0,
        pixelPerfect=False,
        factor=1,
        start=distance + 13,
    )
    houses = cleanLanes(houses)

    road_surface = blocks.get("road_surface")
    structure = blocks.get("structure")

    for lane in roadSurface:
        for xyz in roadSurface[lane]:
            main.fillBlock(
                "air", (xyz[0], xyz[1], xyz[2], xyz[0], xyz[1] + 4, xyz[2])
            )
            main.setBlock(
                random.choices(
                    list(structure.keys()),
                    weights=structure.values(),
                    k=1,
                )[0],
                (xyz[0], xyz[1] - 1, xyz[2]),
            )
            main.setBlock(
                random.choices(
                    list(road_surface.keys()),
                    weights=road_surface.values(),
                    k=1,
                )[0],
                xyz,
            )
            alreadyGenerated.append((xyz[0], xyz[2]))

    lines = blocks.get("lines")
    for lane in roadMarkings:
        for xyz in roadMarkings[lane]:
            if lane == -1:
                main.setBlock(
                    random.choices(
                        list(structure.keys()),
                        weights=structure.values(),
                        k=1,
                    )[0],
                    (xyz[0], xyz[1] - 1, xyz[2]),
                )
                main.setBlock(
                    random.choices(
                        list(lines.keys()),
                        weights=lines.values(),
                        k=1,
                    )[0],
                    (xyz[0], xyz[1], xyz[2]),
                )

    for lane in walkway:
        for xyz in walkway[lane]:
            if lane <= -1:
                counterSegments = 0
                main.fillBlock(
                    "air",
                    (xyz[0], xyz[1] + 1, xyz[2], xyz[0], xyz[1] + 4, xyz[2]),
                )
                main.fillBlock(
                    random.choices(
                        list(structure.keys()),
                        weights=structure.values(),
                        k=1,
                    )[0],
                    (xyz[0], xyz[1] + 1, xyz[2], xyz[0], xyz[1] - 1, xyz[2]),
                )
                alreadyGenerated.append((xyz[0], xyz[2]))

    counterSegments = 0
    for lane in houses:
        for xyz in houses[lane]:
            if lane <= -1:
                counterSegments += 1
                if counterSegments % 10 == 0:
                    housesCoordinates.append((xyz[0], xyz[1], xyz[2]))


def singleLaneRight(XYZ, blocks=standard_modern_lane_composition):
    """Right side."""

    factor = 8
    distance = 2

    roadMarkings = maths.curveSurface(
        np.array(XYZ),
        distance + 1,
        resolution=0,
        pixelPerfect=True,
        factor=1,
        start=2,
    )
    roadMarkings = cleanLanes(roadMarkings)

    roadSurface = maths.curveSurface(
        np.array(XYZ),
        distance,
        resolution=0,
        pixelPerfect=False,
        factor=factor,
    )
    roadSurface = cleanLanes(roadSurface)

    walkway = maths.curveSurface(
        np.array(XYZ),
        distance + 3,
        resolution=0,
        pixelPerfect=False,
        factor=4,
        start=3,
    )
    walkway = cleanLanes(walkway)

    houses = maths.curveSurface(
        np.array(XYZ),
        distance + 14,
        resolution=0,
        pixelPerfect=False,
        factor=1,
        start=distance + 13,
    )
    houses = cleanLanes(houses)

    road_surface = blocks.get("road_surface")
    structure = blocks.get("structure")
    central_lines = blocks.get("central_lines")

    for lane in roadSurface:
        for xyz in roadSurface[lane]:
            main.fillBlock(
                "air", (xyz[0], xyz[1], xyz[2], xyz[0], xyz[1] + 4, xyz[2])
            )
            main.setBlock(
                random.choices(
                    list(structure.keys()),
                    weights=structure.values(),
                    k=1,
                )[0],
                (xyz[0], xyz[1] - 1, xyz[2]),
            )
            main.setBlock(
                random.choices(
                    list(road_surface.keys()),
                    weights=road_surface.values(),
                    k=1,
                )[0],
                xyz,
            )
            alreadyGenerated.append((xyz[0], xyz[2]))

    lines = blocks.get("lines")
    counterSegments = 0
    for lane in roadMarkings:
        for xyz in roadMarkings[lane]:
            if lane == 1:
                main.setBlock(
                    random.choices(
                        list(structure.keys()),
                        weights=structure.values(),
                        k=1,
                    )[0],
                    (xyz[0], xyz[1] - 1, xyz[2]),
                )
                main.setBlock(
                    random.choices(
                        list(lines.keys()),
                        weights=lines.values(),
                        k=1,
                    )[0],
                    (xyz[0], xyz[1], xyz[2]),
                )

            if lane == -1:  # Central Lane.
                counterSegments += 1
                if counterSegments % 4 != 0:
                    main.setBlock(
                        random.choices(
                            list(structure.keys()),
                            weights=structure.values(),
                            k=1,
                        )[0],
                        (xyz[0], xyz[1] - 1, xyz[2]),
                    )
                    main.setBlock(
                        random.choices(
                            list(central_lines.keys()),
                            weights=central_lines.values(),
                            k=1,
                        )[0],
                        (xyz[0], xyz[1], xyz[2]),
                    )
                else:
                    main.setBlock(
                        random.choices(
                            list(structure.keys()),
                            weights=structure.values(),
                            k=1,
                        )[0],
                        (xyz[0], xyz[1] - 1, xyz[2]),
                    )
                    main.setBlock(
                        random.choices(
                            list(road_surface.keys()),
                            weights=road_surface.values(),
                            k=1,
                        )[0],
                        (xyz[0], xyz[1], xyz[2]),
                    )

    for lane in walkway:
        for xyz in walkway[lane]:
            if lane >= 1:
                main.fillBlock(
                    "air",
                    (xyz[0], xyz[1] + 1, xyz[2], xyz[0], xyz[1] + 4, xyz[2]),
                )
                main.fillBlock(
                    random.choices(
                        list(structure.keys()),
                        weights=structure.values(),
                        k=1,
                    )[0],
                    (xyz[0], xyz[1] + 1, xyz[2], xyz[0], xyz[1] - 1, xyz[2]),
                )
                alreadyGenerated.append((xyz[0], xyz[2]))

    counterSegments = 0
    for lane in houses:
        for xyz in houses[lane]:
            if lane >= 1:
                counterSegments += 1
                if counterSegments % 10 == 0:
                    housesCoordinates.append((xyz[0], xyz[1], xyz[2]))


############################ Roads Generator ###########################


class RoadCurve:
    def __init__(self, roadData, XYZ):
        print("road, first input:", XYZ)
        """Create points that forms the lanes depending of the roadData."""
        self.roadData = roadData
        self.XYZ = XYZ

        # Find the offset, where the lanes is.
        self.lanesXYZ = {}
        for __, i in enumerate(self.roadData["lanes"]):
            laneCenterDistance = self.roadData["lanes"][i]["centerDistance"]
            self.lanesXYZ[i] = maths.curveSurface(
                np.array(XYZ),
                abs(laneCenterDistance),
                resolution=0,
                pixelPerfect=True,
                factor=1,
                start=abs(laneCenterDistance) - 1,
                returnLine=False,
            )
            # We only take the desired side.
            if laneCenterDistance == 0:
                self.lanesXYZ[i] = self.lanesXYZ[i][0]
            if laneCenterDistance > 0:
                self.lanesXYZ[i] = self.lanesXYZ[i][1]
            if laneCenterDistance < 0:
                self.lanesXYZ[i] = self.lanesXYZ[i][-1]

    def setLanes(self, lanes=[]):
        """Generate the lanes depending of the function name."""
        for __, i in enumerate(self.roadData["lanes"]):
            if i in lanes or lanes == []:
                self.roadData["lanes"][i]["type"](np.array(self.lanesXYZ[i]))

    def getLanes(self, lanes=[]):
        """Return the points that forms the lanes."""
        lanesDict = {}
        for __, i in enumerate(self.roadData["lanes"]):
            if i in lanes or lanes == []:
                lanesDict[i] = self.lanesXYZ[i]
        return lanesDict


def intersection(
    roadsData, centerPoint, mainRoads, sideRoads
):  # TODO: Refactoring. Error with y in curve.
    """
    [summary]

    [extended_summary]

    Args:
        roadsData (dict): standard_modern_lanes_agencement
        centerPoint (tuple): (x, y, z)
        mainRoads (list): {0:((x, y, z), (x, y, z)), 1:((x, y, z), (x, y, z))}
        sideRoads ([type]): {0:[(x, y, z), 1:(x, y, z), -1:(x, y, z), 2:(x, y, z)}
    """
    # Save all the lanes.
    lanes = {}

    # Set the side roads.
    for i in roadsData["sideRoads"]:
        sideRoad = RoadCurve(
            roadsData["sideRoads"].get(i), (sideRoads.get(i), centerPoint)
        )
        sideRoad.setLanes()
        lanes[sideRoads[i]] = sideRoad.getLanes()

    # Set the main roads.
    for i in roadsData["mainRoads"]:
        mainLanes = []
        mainRoad = RoadCurve(
            roadsData["mainRoads"].get(i), (mainRoads.get(i)[0], centerPoint)
        )
        mainRoad.setLanes()
        lanes[mainRoads[i][0]] = mainRoad.getLanes()
        mainLanes.append(mainRoad.getLanes())
        # We don't want to inverse the orientation of the main road.
        mainRoad = RoadCurve(
            roadsData["mainRoads"].get(i), (centerPoint, mainRoads.get(i)[1])
        )
        mainRoad.setLanes()
        # But we want to save it like the others.
        mainRoad = RoadCurve(
            roadsData["mainRoads"].get(i),
            (
                mainRoads.get(i)[1],
                centerPoint,
            ),
        )
        lanes[mainRoads[i][1]] = mainRoad.getLanes()
        mainLanes.append(mainRoad.getLanes())

        # # Compute the curve of the main road.
        # center = ()
        # for j in list(mainRoad.getLanes().keys()):

        #     line0 = (mainLanes[0][j][0], mainLanes[0][j][1])
        #     line1 = (mainLanes[1][j][0], mainLanes[1][j][1])

        #     intersectionPointsTemp, center = maths.curveCornerIntersectionLine(
        #         line0, line1, 70, angleAdaptation=False, center=center
        #     )

        #     y = 205
        #     intersectionPoints = []
        #     [
        #         intersectionPoints.append((round(xz[0]), y, round(xz[1])))
        #         for xz in intersectionPointsTemp
        #         if (round(xz[0]), y, round(xz[1])) not in intersectionPoints
        #     ]
        #     print(intersectionPointsTemp, center)

        #     singleLane2(
        #         intersectionPoints, blocks=standard_modern_lane_composition
        #     )

    # Sort all the points in rotation order.
    points = []
    points.extend([xyz[i] for xyz in mainRoads.values() for i in range(2)])
    points.extend([xyz for xyz in sideRoads.values()])
    points = maths.sortRotation(points)

    # Compute the curve between each road.
    for i in range(len(points)):
        line0 = (
            lanes[points[i]][max(lanes[points[i]])][0],
            lanes[points[i]][max(lanes[points[i]])][1],
        )
        line1 = (
            lanes[points[i - 1]][min(lanes[points[-1]])][0],
            lanes[points[i - 1]][min(lanes[points[-1]])][1],
        )

        # Compute the curve.
        intersectionPointsTemp = maths.curveCornerIntersectionLine(
            line0, line1, 10, angleAdaptation=False
        )[0]

        y = centerPoint[1]  # Not the real y here
        intersectionPoints = []
        [
            intersectionPoints.append((round(xz[0]), y, round(xz[1])))
            for xz in intersectionPointsTemp
            if (round(xz[0]), y, round(xz[1])) not in intersectionPoints
        ]
        diffAlt = abs(line0[0][1] - line1[0][1])
        maxAlt = max(line0[0][1], line1[0][1])
        print(diffAlt, maxAlt, len(intersectionPoints))
        if diffAlt != 0:
            step = len(intersectionPoints) // diffAlt
        else:
            step = 1
        for i in range(len(intersectionPoints)):
            print(i)
            intersectionPoints[i] = (
                intersectionPoints[i][0],
                maxAlt - (i // step),
                intersectionPoints[i][2],
            )

        singleLaneRight(
            intersectionPoints, blocks=standard_modern_lane_composition
        )

        # # Generate the curve.
        # for key, value in lanes.items():
        #     for __, value1 in value.items():
        #         if intersectionPoints[0] in value1:
        #             # Key found.
        #             for __, j in enumerate(mainRoads):
        #                 if key in mainRoads[j]:
        #                     curveRoad = RoadCurve(
        #                         roadsData["mainRoads"][j], intersectionPoints
        #                     )
        #                     curveRoad.setLanes(
        #                         [max(roadsData["mainRoads"][j]["lanes"])]
        #                     )
        #             # for __, j in enumerate(sideRoads):
        #             #     print(sideRoads[j])
        #             #     if key == sideRoads[j]:
        #             #         print(
        #             #             roadsData["sideRoads"][j], intersectionPoints
        #             #         )
        #             #         curveRoad = Road(
        #             #             roadsData["sideRoads"][j], intersectionPoints
        #             #         )
        #             #         curveRoad.setLanes(
        #             #             [min(roadsData["sideRoads"][j]["lanes"])]
        #             #         )


############################# Lanes Preset #############################


standard_modern_lane_agencement = {
    "lanes": {
        -1: {"type": singleLaneLeft, "centerDistance": -3},
        1: {"type": singleLaneRight, "centerDistance": 3},
    },
}


standard_modern_lanes_agencement = {
    "mainRoads": {
        0: {
            "lanes": {
                -1: {"type": singleLaneLeft, "centerDistance": -5},
                0: {"type": singleLaneLeft, "centerDistance": 0},
                1: {"type": singleLaneRight, "centerDistance": 5},
            }
        },
        1: {
            "lanes": {
                -1: {"type": singleLaneRight, "centerDistance": -5},
                0: {"type": singleLaneRight, "centerDistance": 0},
                1: {"type": singleLaneRight, "centerDistance": 5},
            }
        },
    },
    "sideRoads": {
        0: {
            "lanes": {
                -1: {"type": singleLaneLeft, "centerDistance": -5},
                1: {"type": singleLaneLeft, "centerDistance": 0},
                2: {"type": singleLaneLeft, "centerDistance": 5},
            }
        },
        1: {
            "lanes": {
                -1: {"type": singleLaneLeft, "centerDistance": -5},
                1: {"type": singleLaneLeft, "centerDistance": 0},
                2: {"type": singleLaneLeft, "centerDistance": 5},
            }
        },
    },
}

def findGround(xzStart, xz):  # TODO: Change error.
    """
    Find the surface at xz using heightmap.

    Args:
        xzStart (tuple): Starting coordinates of the heightmap (northwest corner).
        xz (tuple): Coordinates xz in the Minecraft world.

    Returns:
        tuple: Coordinates xyz in the Minecraft world.
    """
    im = Image.open("heightmap.png")
    x = round(xz[0] - xzStart[0])
    z = round(xz[-1] - xzStart[-1])
    # Alpha is defined as the height ([3]).
    width, height = im.size
    if x >= width or z >= height:
        print("img:", x, z)
        print(width, height)
        print(xzStart, xz)
    try:
        return xz[0], (im.getpixel((x, z))[2]) - 1, xz[-1]
    except:
        print("Error getpixel in map.py:42 with ", x, z)
        return None

######

from gdpc import Block as place

import sys
sys.path.append("Terraformer/mapAnalysis/")
import Skeleton 

from gdpc import Editor

from math import sqrt

def get_distance(point1, point2):
    # Calculate the Euclidean distance between two points
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)

def simplify_coordinates(coordinates, epsilon):
    if len(coordinates) < 3:
        return coordinates

    # Find the point with the maximum distance
    max_distance = 0
    max_index = 0
    end_index = len(coordinates) - 1

    for i in range(1, end_index):
        distance = get_distance(coordinates[i], coordinates[0])
        if distance > max_distance:
            max_distance = distance
            max_index = i

    simplified_coordinates = []

    # If the maximum distance is greater than epsilon, recursively simplify
    if max_distance > epsilon:
        rec_results1 = simplify_coordinates(coordinates[:max_index+1], epsilon)
        rec_results2 = simplify_coordinates(coordinates[max_index:], epsilon)

        # Combine the simplified sub-results
        simplified_coordinates.extend(rec_results1[:-1])
        simplified_coordinates.extend(rec_results2)
    else:
        # The maximum distance is less than epsilon, retain the endpoints
        simplified_coordinates.append(coordinates[0])
        simplified_coordinates.append(coordinates[end_index])

    return simplified_coordinates


def irlToMc(coordinates):

    print(coordinates, "coordinates")
    editor = Editor()
    buildArea = editor.getBuildArea()
    xMin = (editor.getBuildArea().begin).x
    yMin = (editor.getBuildArea().begin).y
    zMin = (editor.getBuildArea().begin).z

    print(xMin, yMin, zMin)

    coordinates_final = []

    coordinates_final.append(coordinates[0] + xMin)
    coordinates_final.append(coordinates[1] + yMin)
    coordinates_final.append(coordinates[2] + zMin)

    print(coordinates_final)

    return coordinates_final

def setRoads(skeleton):
    # Generation
    for i in range(len(skeleton.lines)):
        for j in range(len(skeleton.lines[i])):
            xyz = irlToMc(skeleton.coordinates[skeleton.lines[i][j]])
            skeleton.lines[i][j] = xyz
            print(skeleton.lines[i][j], "eee")

    # Simplification

    for i in range(len(skeleton.lines)):
        skeleton.lines[i] = simplify_coordinates(skeleton.lines[i], 10)


    for i in range(len(skeleton.lines)):  # HERE --------------------------------------
        print(skeleton.lines[i])
        road = RoadCurve(standard_modern_lane_agencement, skeleton.lines[i])
        road.setLanes()
        print(road.getLanes(), "LANES ***********")

    rejected = []
    accepted = []
    # print(housesCoordinates)
    for i in range(len(housesCoordinates)):
        pos = housesCoordinates[i]
        # print(pos, "pos0")
        editor = Editor()
        xMin = (editor.getBuildArea().begin).x
        yMin = (editor.getBuildArea().begin).y
        zMin = (editor.getBuildArea().begin).z
        base = findGround((xMin, zMin), pos)
        if base != None:
            # print(pos, "pos1")
            pos1 = (
                pos[0] - random.randint(3, 6),
                base[1],
                pos[2] - random.randint(3, 6),
            )
            pos2 = (
                pos[0] + random.randint(3, 6),
                base[1],
                pos[2] + random.randint(3, 6),
            )
            pos3 = (
                pos1[0],
                base[1],
                pos2[2],
            )
            pos4 = (
                pos2[0],
                base[1],
                pos1[2],
            )
            # print(pos1, pos2, pos3, pos4, "pos")
            xMin = (editor.getBuildArea().begin).x
            yMin = (editor.getBuildArea().begin).y
            zMin = (editor.getBuildArea().begin).z
            Ypos1 = findGround((xMin, zMin), pos1)
            Ypos2 = findGround((xMin, zMin), pos2)
            Ypos3 = findGround((xMin, zMin), pos3)
            Ypos4 = findGround((xMin, zMin), pos4)

            if (
                Ypos1 != None
                and Ypos2 != None
                and Ypos3 != None
                and Ypos4 != None
            ):

                pos2 = (
                    pos2[0],
                    max(Ypos1[1], Ypos2[1], base[1], Ypos3[1], Ypos4[1]),
                    pos2[2],
                )
                pos1 = (
                    pos1[0],
                    max(Ypos1[1], Ypos2[1], base[1], Ypos3[1], Ypos4[1]),
                    pos1[2],
                )
                if (
                    (pos1[0], pos1[2]) not in alreadyGenerated
                    and (
                        pos2[0],
                        pos2[2],
                    )
                    not in alreadyGenerated
                    and (pos1[0], pos2[2]) not in alreadyGenerated
                    and (pos2[0], pos1[2])
                ):  # HERE, remove print and find why house gen on self

                    for xi in range(
                        -5,
                        (max(pos1[0], pos2[0]) - min(pos1[0], pos2[0])) + 5,
                    ):
                        for yi in range(
                            -5,
                            (max(pos1[2], pos2[2]) - min(pos1[2], pos2[2]))
                            + 5,
                        ):
                            alreadyGenerated.append(
                                (
                                    min(pos1[0], pos2[0]) + xi,
                                    min(pos1[2], pos2[2]) + yi,
                                )
                            )

                    nb_style=randint(0,3)
                    door = ["left", "right"]
                    r2 = random.randint(0, 1)
                    facing = ["south", "north", "east", "west"]
                    r3 = random.randint(0, 3)
                    
                    house.house(pos1,pos2,door[r2], 10, nb_style, facing[r3])
                    accepted.append(
                        (
                            pos1[0],
                            pos1[2],
                            pos2[0],
                            pos2[2],
                        )
                    )
                else:
                    rejected.append(
                        (
                            pos1[0],
                            pos1[2],
                            pos2[0],
                            pos2[2],
                        )
                    )

    print("Done")


# ### Execution ###


# from skimage.data import binary_blobs
# blobs = binary_blobs(16, volume_fraction=0.3, n_dim=3)

# # # # # # #

import sys
sys.path.append("Terraformer/dataAcquisition/")
import World

w = World.World()

import sys
sys.setrecursionlimit(w.length_x * w.length_y * w.length_z)

w.propagate((1754, 67, 635)) # Change here.
print("done")
print(w.binaryImage())

# # # # # #

skel = Skeleton.Skeleton()

skel.setSkeleton(w.binaryImage())

skel.parseGraph()
print(skel.centers)
print(skel.lines)
print(skel.intersections)
print(skel.coordinates)

Skeleton.heightmap()

setRoads(skel)