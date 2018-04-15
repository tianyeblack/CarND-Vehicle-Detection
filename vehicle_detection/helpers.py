import glob
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def load_images():
    images = glob.iglob('dataset/**/*.png', recursive=True)
    cars = []
    not_cars = []
    for i in images:
        img = mpimg.imread(i)
        not_cars.append(img) if 'non-vehicles' in i else cars.append(img)
    return cars, not_cars


def visualize(rows, columns, images, titles, figure_size):
    fig, axes = plt.subplots(rows, columns, squeeze=False, figsize=figure_size)
    for r in range(len(images)):
        for c in range(len(images[r])):
            image_dimensions_length = len(images[r][c].shape)
            if image_dimensions_length < 3:
                axes[r][c].imshow(images[r][c], cmap='hot')
                axes[r][c].set_title(titles[r][c])
            else:
                axes[r][c].imshow(images[r][c])
                axes[r][c].set_title(titles[r][c])
