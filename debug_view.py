from PIL import Image

def generate_top_view_image(array_3d):
    width = len(array_3d)
    height = len(array_3d[0][0])
    
    image = Image.new("1", (width, height), color=1)  # Créer une image blanche
    
    for x in range(width):
        for z in range(height):
            for y in range(len(array_3d[0])):
                if array_3d[x][y][z]:
                    image.putpixel((x, z), 0)  # Si au moins un True, mettre le pixel en noir
                    break  # Sortir de la boucle si True est trouvé
    
    return image



if __name__=="__main__":
    # Exemple d'utilisation
    array_3d = [
        [[True, False, False], [False, True, False], [False, False, False]],
        [[False, False, False], [True, True, True], [False, False, False]],
        [[False, False, False], [False, True, False], [False, False, False]]
    ]

    image = generate_top_view_image(array_3d)
    image.save("top_view_image.png")