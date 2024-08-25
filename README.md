# Image Processing with Multithreading and Multiprocessing
This is a Python program for processing images with multithreading and multiprocessing. The program takes in a list of image paths, the number of processes to use, and the number of threads to use per process. It then splits each image into sub-images and processes each sub-image in parallel using threads, and each image in parallel using processes.

#### Dependencies
This program uses the following Python libraries:
* opencv-python (cv2)
* numpy
* os, if required
* concurrent.futures
* multiprocessing

#### How to use
* Ensure that all dependencies are installed on your system.
* Place the images you want to process in the same directory as the program file.
* Open the program file and modify the image_paths, num_procs, and num_threads variables to your desired values.
* Run the program.
Note: If you want to get files from a specific directory, uncomment the image_paths variable in the main block and modify the directory path accordingly.

#### Functionality
The program performs the following steps:
* Reads in each image from the given list of image paths.
* Splits each image into sub-images based on the number of threads to use.
* Processes each sub-image in parallel using threads.
* Combines the processed sub-images to form the processed image.
* Writes the processed image to disk.
* The program uses multiprocessing to process each image in parallel, and multithreading to process each sub-image in parallel. This approach allows for efficient use of system resources and faster processing times for large images.

#### Execute the program
* Run the program using the command `python3 main.py` in linux
