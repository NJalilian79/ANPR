▎Automatic Number Plate Recognition (ANPR) Project

▎Overview

This project implements a simple Automatic Number Plate Recognition (ANPR) system using OpenCV and Python. The primary goal is to detect and extract the license plate from a given image, enabling further processing or recognition of the plate characters.

▎Features

- Image Preprocessing: Converts the input image to grayscale and applies bilateral filtering to reduce noise while preserving edges.
- Edge Detection: Utilizes the Canny edge detection algorithm to highlight the contours of potential license plates.
- Contour Detection: Identifies contours in the edged image and filters them based on size to locate the license plate.
- License Plate Extraction: Draws contours around the detected license plate and extracts it for further analysis.

▎Requirements

To run this project, ensure you have the following libraries installed:

- OpenCV
- NumPy
- Matplotlib
- imutils

You can install these dependencies using pip:

pip install opencv-python numpy matplotlib imutils


▎How to Use

1. Place your target image (e.g., image5.jpg) in the project directory.
2. Run the script to process the image:
      python anpr.py
   
3. The program will display the processed images, including the grayscale version, edges detected, and the cropped license plate.

▎Code Explanation

1. Image Loading: The image is read using OpenCV and converted to grayscale for easier processing.
2. Bilateral Filter: This filter smooths the image while maintaining edges, which is crucial for effective edge detection.
3. Canny Edge Detection: Edges are detected to identify potential contours.
4. Contour Detection: The contours are sorted based on area, and the largest four-sided contour is assumed to be the license plate.
5. Orientation Calculation: The orientation of the detected license plate is calculated for further analysis.
6. Cropping: The detected license plate region is cropped from the original image for display.

▎Visualizations

The project utilizes Matplotlib to visualize intermediate steps, helping users understand how the algorithm processes the image at each stage.

▎Future Work

- Implement character recognition on the extracted license plate using Optical Character Recognition (OCR) techniques.
- Enhance accuracy by integrating machine learning models for better detection.
- Create a user-friendly interface for uploading images and displaying results.

▎Contributing

Feel free to fork this repository and submit pull requests for enhancements or bug fixes. Your contributions are welcome!
