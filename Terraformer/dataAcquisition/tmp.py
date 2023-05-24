from gdpc import Editor, Block, geometry
import numpy as np
import math

def compute_normals(points):
    # Calculer les vecteurs entre les points adjacents
    vectors = points[1:] - points[:-1]

    # Calculer les produits croisés des vecteurs adjacents
    cross_products = np.cross(vectors[:-1], vectors[1:])

    # Normaliser les vecteurs croisés pour obtenir les normales
    normals = cross_products / np.linalg.norm(cross_products, axis=1)[:, np.newaxis]

    return normals

# Exemple d'utilisation
# points est un tableau numpy de la forme (N, 3) où N est le nombre de points
points = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 1]])
normals = compute_normals(points)

# Affichage des normales pour chaque point
for i, normal in enumerate(normals):
    print(f"Point {i+1}: Normal = {normal}")

# import numpy as np
# from scipy.spatial import Delaunay

# def extract_surface_points(points, triangles):
#     surface_points = []
#     for triangle in triangles:
#         surface_points.extend(points[triangle[:3]])
#     return np.unique(surface_points, axis=0)

# # Exemple d'utilisation
# # points est un tableau numpy de la forme (N, 3) où N est le nombre de points
# points = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 1], [0, 1, 1], [0.5, 0.5, 0.2]])
# tri = Delaunay(points[:, :2])  # Utiliser uniquement les coordonnées x et y

# surface_points = extract_surface_points(points, tri.simplices)

# print("Surface Points:")
# print(surface_points)

# import numpy as np
# from scipy.spatial import Delaunay

# # Points représentant la surface dans l'espace 3D
# points = np.array([[2009, 81, 676], [2010, 81, 676], [2011, 81, 676], [2009, 80, 677], [2010, 80, 677], [2011, 80, 677], [2009, 79, 678], [2010, 79, 678], [2011, 79, 678]])

# # Triangulation
# tri = Delaunay(points)

# # Obtention des indices des sommets pour chaque triangle
# tri_indices = tri.simplices

# print("hello")
# print(tri_indices)

# from scipy.spatial import ConvexHull

# hull = ConvexHull(points)
# indices = hull.simplices
# vertices = points[indices]

# print("ttttttttttttttt")
# print(vertices)

import numpy as np
import matplotlib.pyplot as plt
# Defining variables

points = np.array([[2009, 81, 676], [2010, 85, 676], [2011, 81, 676], [2009, 80, 677], [2010, 80, 677], [2011, 80, 677], [2009, 79, 678], [2010, 79, 678], [2011, 79, 678]])

# Transposer le tableau
transposed_points = points.transpose()

# Extraire les listes x, y et z
x = transposed_points[0].tolist()
y = transposed_points[1].tolist()
z = transposed_points[2].tolist()

# Creating figure and 3D axes
fig = plt.figure(figsize =(9, 5))
ax = plt.axes(projection ='3d')
# Creating plot
ax.plot_trisurf(x, y, z)
plt.show()

# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import mpl_toolkits.mplot3d as a3
# import numpy as np
# import scipy as sp
# from scipy import spatial as sp_spatial


# def icosahedron():
#     h = 0.5*(1+np.sqrt(5))
#     p1 = np.array([[0, 1, h], [0, 1, -h], [0, -1, h], [0, -1, -h]])
#     p2 = p1[:, [1, 2, 0]]
#     p3 = p1[:, [2, 0, 1]]
#     return np.vstack((p1, p2, p3))


# def cube():
#     points = np.array([
#         [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
#         [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1],
#     ])
#     return points


# # points = icosahedron()
# # points = cube()

# hull = sp_spatial.ConvexHull(points)
# indices = hull.simplices
# faces = points[indices]

# print('area: ', hull.area)
# print('volume: ', hull.volume)
# print(hull.vertices)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri

# points = np.array([[2009, 81, 676], [2010, 81, 676], [2011, 81, 676], [2009, 80, 677], [2010, 80, 677], [2011, 80, 677], [2009, 79, 678], [2010, 79, 678], [2011, 79, 678]])

# Transposer le tableau
transposed_points = points.transpose()

# Extraire les listes x, y et z
x = transposed_points[0].tolist()
y = transposed_points[1].tolist()
z = transposed_points[2].tolist()

# Créer la triangulation
triang = mtri.Triangulation(y, z)

# Récupérer les indices des triangles
triangles = triang.triangles

print(triangles)


coordonnees = [points.tolist()[triangles[i][j]] for i in range(len(triangles)) for j in range(len(triangles[i]))]

print(coordonnees)

normals = compute_normals(np.array(coordonnees))

# Affichage des normales pour chaque point
for i, normal in enumerate(normals):
    print(f"Point {i+1}: Normal = {normal}")