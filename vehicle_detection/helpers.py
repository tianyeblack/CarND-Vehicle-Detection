import glob
import matplotlib.image as mpimg


def load_images():
    images = glob.iglob('dataset/**/*.png', recursive=True)
    cars = []
    not_cars = []
    for i in images:
        img = mpimg.imread(i)
        not_cars.append(img) if 'non-vehicles' in i else cars.append(img)
    return cars, not_cars
