# Satellite Image Change Detection Using Image Processing

A Python-based image-processing project that detects pixel-level differences between satellite images captured at different points in time.

This project explores how classical image-processing techniques can be used to identify visual changes in satellite imagery, generate binary change masks, and highlight detected differences.

## Project Overview

The project compares satellite images of the same geographical area acquired on different dates. It uses a pixel-based change detection pipeline to identify areas where image intensities differ.

The primary experiment uses Sentinel-2 imagery of Bengaluru, India. A second image pair from New York City is used to test the general-purpose detection function on another location.

## Objectives

- Compare images of the same area captured at different times.
- Calculate pixel-wise absolute differences.
- Apply thresholding to identify significant differences.
- Reduce small isolated detections using morphological operations.
- Visualize detected changes with binary masks and highlighted overlays.
- Examine how threshold selection affects the detected change percentage.

## Methodology

1. **Image loading:** Load the two satellite images.
2. **Grayscale conversion:** Convert RGB images to grayscale.
3. **Absolute difference:** Calculate the pixel-wise intensity difference between the images.
4. **Thresholding:** Separate pixels with differences above the selected threshold.
5. **Morphological opening:** Reduce small isolated detections using a 3 × 3 kernel.
6. **Visualization:** Display the difference image, binary change mask, and highlighted overlay.
7. **Threshold analysis:** Compare detection percentages at different threshold values.

## Experiments

### Bengaluru, India

- Earlier image: 18 January 2023
- Later image: 22 January 2026
- Nominal image resolution: 10 metres per pixel
- Image dimensions: 290 × 215 pixels
- Baseline threshold: 30

With the selected processing settings, **6.07% of pixels were marked as changed**. This is an algorithmic detection result, not a verified measurement of urban expansion.

Threshold sensitivity was also examined:

| Threshold | Detected pixel percentage |
|---:|---:|
| 15 | 15.63% |
| 30 | 6.07% |
| 50 | 2.17% |

### New York City

A second image pair is used to test the generalized detection function on another geographical area. Refer to the notebook for the experiment's implementation and outputs.

## Technologies Used

- Python
- Jupyter Notebook
- OpenCV
- NumPy
- Matplotlib
- tifffile

## Running the Project

Install the required packages:

```bash
pip install numpy matplotlib opencv-python tifffile pandas jupyter
```

Then open the notebook in Jupyter and run its cells in order.

The satellite TIFF files are not included in this repository. Download the corresponding imagery from the original provider and update the file paths in the notebook if necessary.

## Data Source

Bengaluru imagery was obtained through the [Copernicus Data Space Browser](https://dataspace.copernicus.eu/browser/), using Sentinel-2 Level-2A true-colour imagery.

Check the applicable data terms and attribution requirements before redistributing downloaded imagery.

## Limitations

- Pixel differences do not necessarily represent real-world construction or land-use change.
- Image misalignment can generate false detections.
- Shadows, haze, atmospheric conditions, vegetation changes, and illumination differences can affect the output.
- The detected percentage depends on the threshold and preprocessing settings.
- The current experiments do not establish accuracy against ground-truth labels.

## Future Improvements

- Apply explicit image registration before comparison.
- Explore alternative difference metrics and colour spaces.
- Evaluate the detection results against manually labelled reference data.
- Investigate multispectral imagery for more informative change detection.

## Project Status

Academic mini-project developed to explore temporal satellite image change detection using classical image-processing techniques.
