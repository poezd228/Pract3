import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from skimage import measure

# Загрузка изображения
image = plt.imread('your_image.jpg')

# Преобразование изображения в оттенки серого
gray_image = np.mean(image, axis=2)

# Построение контуров объектов на изображении
contours = measure.find_contours(gray_image, 0.5)

# Создание массива точек, представляющих центры масс каждого контура
points = []
for contour in contours:
    cy, cx = np.mean(contour, axis=0)
    points.append([cx, cy])

# Преобразование массива точек в формат, подходящий для построения диаграммы Вороного
points = np.array(points)

# Построение диаграммы Вороного
vor = Voronoi(points)

# Визуализация изображения
plt.imshow(image)

# Визуализация диаграммы Вороного
voronoi_plot_2d(vor, show_vertices=False, line_colors='r', line_width=1)

plt.title('Voronoi Diagram')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
