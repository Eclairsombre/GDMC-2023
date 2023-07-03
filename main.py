import World
import Skeleton
import mapAnalysis
from PIL import Image
import numpy as np

import debug_view
import roads


world = World.World()
heightmap, watermap, treesmap = world.getData()

heightmap.save('data/heightmap.png')
watermap.save('data/watermap.png')
treesmap.save('data/treesmap.png')

mapAnalysis.applyFilters()


world.maskVolume('data/combinedMap_erroded.png')

main_axis = Skeleton.Skeleton()

volume = world.volumeTo3DBinaryImage()

debug_view.generate_top_view_image(volume).save("data/top_view_image2.png")

main_axis.setSkeleton(volume)


main_axis.parseGraph()

# print(main_axis.centers)
# print('--1-------------------------------------')
# print(main_axis.lines)
# print('--2-------------------------------------')
# print(main_axis.intersections)
# print('--3-------------------------------------')
# print(main_axis.coordinates)

heightmap_skeleton, roadsArea = main_axis.map()
heightmap_skeleton.save('data/skeleton.png')

roadsArea.save('data/roadsArea.png')
mapAnalysis.roadsArea('data/roadsArea.png')

mapAnalysis.removeTrees('data/treesmap.png', 'data/roadsArea.png', 'data/heightmap.png')

mapAnalysis.combineMaps('data/heightmap.png', 'data/roadsArea.png', value=0).save('data/heightmap_roads.png')
mapAnalysis.smoothRoads('data/heightmap.png').save('data/heightmap_roads_smooth.png')
mapAnalysis.smoothTerrain('data/heightmap.png', 'data/heightmap_roads_smooth.png', 'data/roadsArea.png').save('data/heightmap_delta.png')
roads.setRoads(main_axis)