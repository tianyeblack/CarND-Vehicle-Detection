# Writeup

## **Vehicle Detection Project**

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector.
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: ./output_images/car_not_car.png
[image2]: ./output_images/HOG_example.png
[image3]: ./output_images/sliding_windows.png
[image4]: ./output_images/sliding_window.png
[image5]: ./output_images/bboxes_and_heat.png
[image6]: ./output_images/labels_map.png
[image7]: ./output_images/output_bboxes.png
[video1]: ./project_video_output.mp4

## [Rubric](https://review.udacity.com/#!/rubrics/513/view) Points

Here I will consider the rubric points individually and describe how I addressed each point in my implementation.

---

### 1. README

#### Provide a Writeup / README that includes all the rubric points and how you addressed each one

This is it

### 2. Histogram of Oriented Gradients (HOG)

#### Explain how (and identify where in your code) you extracted HOG features from the training images

The code for this step is contained in the first to the 4th code cell of the IPython notebook.

I started by reading in all the `vehicle` and `non-vehicle` images.  Here is an example of one of each of the `vehicle` and `non-vehicle` classes:

![alt text][image1]

I then explored different color spaces and different `skimage.feature.hog()` parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).  I grabbed random images from each of the two classes and displayed them to get a feel for what the `skimage.feature.hog()` output looks like.

Here is an example using the `YCrCb` color space and HOG parameters of `orientations=9`, `pixels_per_cell=(8, 8)` and `cells_per_block=(2, 2)`:

![alt text][image2]

#### Explain how you settled on your final choice of HOG parameters

I tried various combinations of parameters and chose `orientations=9`, `pixels_per_cell=(8, 8)` and `cells_per_block=(2, 2)` for these reasons:

1. Orientations smaller than 9 do not indicate the gradients very clearly, the ones larger than 9 do not have more details than 9
2. Since there are 64 pixels in each dimension, possible candidates for pixels per cell are 2, 4, 8, 16. 8 is a good balance between feature numbers and efficiency, with 4 too many features but not more details and 16 too few details
3. For cells per block, 2 is chosen for its balance of normalization effect and efficiency

#### Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them)

I trained a linear SVM using GridSearchCV in the 6th code cell. I searched linear and radial basis function kernels combined with different penalty score for errors. The features are extracted with `single_image_features_method` configured by `configure_single_image_features`.

### 3. Sliding Window Search

#### Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows

I took a look at the test pictures and realize the cars were only going to be between 400 and 656. The range is selected also to divide up the windows nicely. For cars further in the background, they are usually really small, less than 60 pixels, which requires windows smaller than 64. 48 was chosen for it's small enough to capture the cars far away but not too small to have too many windows to search. On the other hand, for cars that are close, window should be large enough to fit in significant portion of the car to identify.

Window overlap ratio is 0.5, also for similar reasons. Too small may result in missing identifying cars, too large creates too many windows and slow down the processing.

![alt text][image3]

#### Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier

Ultimately I searched on 4 scales using YCrCb 3-channel HOG features plus spatially binned color and histograms of color in the feature vector, which provided a nice result.  Here are some example images:

![alt text][image4]

### 4. Video Implementation

#### Provide a link to your final video output

Here's a [link to my video result][video1]

#### Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes

In code box 15, I recorded the positions of positive detections in each frame of the video. From the positive detections I created a heatmap (using method `accumulate_heat` in the 12th code box) and then thresholded that map (with `thresholding` method in the same box) to identify vehicle positions. I then used `scipy.ndimage.measurements.label()` to identify individual blobs in the heatmap and assumed each blob corresponded to a vehicle. In the end, I constructed bounding boxes to cover the area of each blob detected in method `draw_labeled_bounding_boxes`.

Here's an example result showing the heatmap from a series of frames of video, the result of `scipy.ndimage.measurements.label()` and the bounding boxes then overlaid on the last frame of video:

**Here are six frames and their corresponding heatmaps:**b

![alt text][image5]

**Here is the output of `scipy.ndimage.measurements.label()` on the integrated heatmap from all six frames:**

![alt text][image6]

**Here the resulting bounding boxes are drawn onto the last frame in the series:**

![alt text][image7]

---

### Discussion

**Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?**

1. One of the main issue is false positives, although using Grid Search with Cross-Validation allow the classfier to be really accurate on training and test sets, still there are significant number of flase positives. Averaging across multiple frames helped a lot, eliminated most of them.
2. When vehicles are far away, they become harder to detect as there may not be enough features to identify that vehicle in a window. Therefore, thresholding cannot be too high, otherwise, the vehicle may not get identified at all
3. The pipeline would very likely fail if the video is changed. The classifier fits the dataset too well and a lot of parameters need to be adjusted to match the camera position and calibrations. Gathering more data in different weather conditions and situations would help the classifier generalize. Using a more complicated one like CNN would also generalize better and thus more accurate in other examples.
