import cv2
import numpy as np

COLOR_CONVERSION_CONSTANTS = {
    'HSV': cv2.COLOR_RGB2HSV,
    'LUV': cv2.COLOR_RGB2LUV,
    'HLS': cv2.COLOR_RGB2HLS,
    'YUV': cv2.COLOR_RGB2YUV,
    'YCrCb': cv2.COLOR_RGB2YCrCb
}

COLOR_SPACE = 'YCrCb'
PIXEL_PER_CELL = 8
CELL_PER_BLOCK = 2
ORIENTATION = 9
HOG_CHANNEL = "ALL"  # Can be 0, 1, 2, or "ALL"
SPATIAL_SIZE = (16, 16)  # Spatial binning dimensions
HISTOGRAM_BINS = 16  # Number of histogram bins
SPATIAL_FEATURE = True  # Spatial features on or off
HISTOGRAM_FEATURE = True  # Histogram features on or off
HOG_FEATURE = True  # HOG features on or off
Y_START_AND_STOPS = [(400, 464), (400, 528), (400, 592), (400, 656)]  # Min and max in y to search in slide_window()
SLIDING_WINDOW_SIZES = [(48, 48), (64, 64), (96, 96), (128, 128)]
OVERLAP_RATIOS = zip(np.arange(0.5, 0.7, 0.05), np.arange(0.5, 0.7, 0.05))
SLIDING_WINDOW_PARAMS = list(zip(Y_START_AND_STOPS, SLIDING_WINDOW_SIZES, OVERLAP_RATIOS))
WINDOW_CACHE_LENGTH = 10
HEATMAP_THRESHOLD = 13
