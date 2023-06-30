from PIL import Image
from PIL import ImageFilter
from gdpc import Editor
import numpy as np
from scipy import ndimage
import tools

from skimage import morphology



def filterSobel(input):
    """
    Edge detection algorithms from an image.

    Args:
        input (image): image to filter
    """

    # Open the image
    img = np.array(Image.open(input).convert('RGB')).astype(np.uint8)

    # Apply gray scale
    gray_img = np.round(
        0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]
    ).astype(np.uint8)

    # Sobel Operator
    h, w = gray_img.shape
    # define filters
    horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # s2
    vertical = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  # s1

    # define images with 0s
    newhorizontalImage = np.zeros((h, w))
    newverticalImage = np.zeros((h, w))
    newgradientImage = np.zeros((h, w))

    # offset by 1
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            horizontalGrad = (
                (horizontal[0, 0] * gray_img[i - 1, j - 1])
                + (horizontal[0, 1] * gray_img[i - 1, j])
                + (horizontal[0, 2] * gray_img[i - 1, j + 1])
                + (horizontal[1, 0] * gray_img[i, j - 1])
                + (horizontal[1, 1] * gray_img[i, j])
                + (horizontal[1, 2] * gray_img[i, j + 1])
                + (horizontal[2, 0] * gray_img[i + 1, j - 1])
                + (horizontal[2, 1] * gray_img[i + 1, j])
                + (horizontal[2, 2] * gray_img[i + 1, j + 1])
            )

            newhorizontalImage[i - 1, j - 1] = abs(horizontalGrad)

            verticalGrad = (
                (vertical[0, 0] * gray_img[i - 1, j - 1])
                + (vertical[0, 1] * gray_img[i - 1, j])
                + (vertical[0, 2] * gray_img[i - 1, j + 1])
                + (vertical[1, 0] * gray_img[i, j - 1])
                + (vertical[1, 1] * gray_img[i, j])
                + (vertical[1, 2] * gray_img[i, j + 1])
                + (vertical[2, 0] * gray_img[i + 1, j - 1])
                + (vertical[2, 1] * gray_img[i + 1, j])
                + (vertical[2, 2] * gray_img[i + 1, j + 1])
            )

            newverticalImage[i - 1, j - 1] = abs(verticalGrad)

            # Edge Magnitude
            mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
            newgradientImage[i - 1, j - 1] = mag

    image = Image.fromarray(newgradientImage)
    image = image.convert("L")
    # image = image.convert("I")

    return image



def filterSmooth(input):
    """
    Args:
        input (image): white and black image representing the derivative of the terrain (sobel), where black is flat and white is very steep.

    Returns:
        image: black or white image, with black as flat areas to be skeletonize
    """

    image = Image.open(input)

    # image = image.filter(ImageFilter.SMOOTH_MORE)
    # image = image.filter(ImageFilter.SMOOTH_MORE)
    # image = image.filter(ImageFilter.SMOOTH_MORE)
    image = image.filter(ImageFilter.GaussianBlur(radius=3))
    array = np.array(image)

    bool_array = array > 7

    # bool_array = ndimage.binary_opening(bool_array, structure=np.ones((3,3)), iterations=1)
    # bool_array = ndimage.binary_closing(bool_array, structure=np.ones((3,3)), iterations=1)
    # bool_array = ndimage.binary_opening(bool_array, structure=np.ones((5,5)), iterations=1)
    # bool_array = ndimage.binary_closing(bool_array, structure=np.ones((5,5)), iterations=1)
    # bool_array = ndimage.binary_opening(bool_array, structure=np.ones((7,7)), iterations=1)
    # bool_array = ndimage.binary_closing(bool_array, structure=np.ones((7,7)), iterations=1)

    return Image.fromarray(bool_array)

def filterSmoothExtended(input):
    """
    Smooth the watermap and extended the water area in ordre to overlap with the sobel map. 

    Args:
        input (image): white and black image representing the derivative of the terrain (sobel), where black is flat and white is very steep.

    Returns:
        image: black or white image, with black as flat areas to be skeletonize
    """

    image = Image.open(input)

    image = image.filter(ImageFilter.GaussianBlur(radius=2))
    array = np.array(image)

    bool_array = array > 1


    return Image.fromarray(bool_array)



def combineMaps(sobel_smooth, watermap, value=255):
    editor = Editor()
    buildArea = editor.getBuildArea()
    buildRect = buildArea.toRect()

    xzStart = buildRect.begin
    xzDistance = (max(buildRect.end[0], buildRect.begin[0]) - min(buildRect.end[0], buildRect.begin[0]), max(buildRect.end[1], buildRect.begin[1]) - min(buildRect.end[1], buildRect.begin[1]))
    combinedMap = Image.open(sobel_smooth)
    watermap = Image.open(watermap)

    for x in range(0, xzDistance[0]):
        for z in range(0, xzDistance[1]):
            if watermap.getpixel((x, z)) == (value):
                combinedMap.putpixel((x, z), (255))
    
    return combinedMap



def applyFilters():
    filterSobel('data/heightmap.png').save('data/sobel.png')
    filterSmooth('data/sobel.png').save('data/sobel_smooth.png')
    filterSmoothExtended('data/watermap.png').save('data/watermap_smooth.png')

    array = np.array(Image.open('data/watermap_smooth.png'))
    array = ndimage.binary_dilation(array, iterations=5)
    Image.fromarray(array).save('data/watermap_smooth_extended.png')

    combineMaps('data/sobel_smooth.png', 'data/watermap_smooth.png').save('data/combinedMap.png')

    array = np.array(Image.open('data/combinedMap.png'))
    array = ndimage.binary_erosion(array, iterations=5)
    array = ndimage.binary_dilation(array, iterations=5)
    Image.fromarray(array).save('data/combinedMap_erroded.png')

def roadsArea(input):
    array = np.array(Image.open(input))
    array = ndimage.binary_dilation(array, iterations=12)
    Image.fromarray(array).save(input)

def smoothRoads(input):
    image = Image.open(input).convert("RGB")
    image = image.filter(ImageFilter.GaussianBlur(radius=3))
    return image

def smoothTerrain(heightmap, heightmap_smooth, mask):
        """
        Generate all needed datas for the generator : heightmap, watermap, and preset the volume with data from the heightmap.
        """

        editor = Editor()
        buildArea = editor.getBuildArea()
        buildRect = buildArea.toRect()

        xzStart = buildRect.begin
        print(xzStart, "xzStart")
        xzDistance = (max(buildRect.end[0], buildRect.begin[0]) - min(buildRect.end[0], buildRect.begin[0]), max(buildRect.end[1], buildRect.begin[1]) - min(buildRect.end[1], buildRect.begin[1]))

        heightmap = Image.open(heightmap)
        heightmap_smooth = Image.open(heightmap_smooth)
        mask = Image.open(mask)

        slice = editor.loadWorldSlice(buildRect)


        for x in range(0, xzDistance[0]):
            for z in range(0, xzDistance[1]):
                
                if mask.getpixel((x, z))!= 0 : #mask
                    y = heightmap.getpixel((x, z))[0]
                    ySmooth = heightmap_smooth.getpixel((x, z))[-1]
                    delta = y - ySmooth
                    heightmap.putpixel((x, z), delta)

                    if delta != 0:
                        print('getData', xzStart[0] + x, y, xzStart[1] + z)
                        block = slice.getBlock((x, y, z))
                        if delta > 0:
                            tools.fillBlock('minecraft:air', (xzStart[0] + x, y, xzStart[1] + z, xzStart[0] + x, ySmooth, xzStart[1] + z))
                            tools.setBlock(block.id, (xzStart[0] + x, ySmooth, xzStart[1] + z))
                            
                            # print("setblock", xzStart[0] + x, ySmooth, xzStart[1] + z, block.id)
                        else:
                            tools.fillBlock(block.id, (xzStart[0] + x, y, xzStart[1] + z, xzStart[0] + x, ySmooth, xzStart[1] + z))
        
        return heightmap

def removeTrees(treesmap, roadsArea, heightmap):
        """
        Generate all needed datas for the generator : heightmap, watermap, and preset the volume with data from the heightmap.
        """

        editor = Editor()
        buildArea = editor.getBuildArea()
        buildRect = buildArea.toRect()

        xzStart = buildRect.begin
        print(xzStart, "xzStart")
        xzDistance = (max(buildRect.end[0], buildRect.begin[0]) - min(buildRect.end[0], buildRect.begin[0]), max(buildRect.end[1], buildRect.begin[1]) - min(buildRect.end[1], buildRect.begin[1]))

        heightmap = Image.open(heightmap)
        treesmap = Image.open(treesmap).convert('L')
        roadsArea = Image.open(roadsArea)

        slice = editor.loadWorldSlice(buildRect)


        for x in range(0, xzDistance[0]):
            for z in range(0, xzDistance[1]):
                liste = []
                if roadsArea.getpixel((x, z)) == 255 : #mask
                    if treesmap.getpixel((x, z)) > 0 : #mask
                        liste.append((x, z))
                        # print(treesmap.getpixel((x, z)))
                        y = heightmap.getpixel((x, z))[0]
                        yTree = treesmap.getpixel((x, z))

                        # tools.fillBlock("minecraft:air", (xzStart[0] + x, y+1, xzStart[1] + z, xzStart[0] + x, yTree, xzStart[1] + z))
                        
                        treeArea = morphology.flood(treesmap, (z, x), tolerance=1)
                        Image.fromarray(treeArea).save('data/flood.png')

                        for i in range(0, xzDistance[0]):
                            for j in range(0, xzDistance[1]):
                                print(x, z)
                                if list(treeArea)[j][i]:
                                    
                                    y = heightmap.getpixel((i, j))[0]
                                    yTree = treesmap.getpixel((i, j))
                                    treesmap.putpixel((i, j), 0)
                                    tools.fillBlock("minecraft:air", (xzStart[0] + i, y+1, xzStart[1] + j, xzStart[0] + i, yTree, xzStart[1] + j))
                print(liste)