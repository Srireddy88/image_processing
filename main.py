import concurrent.futures
import numpy as np
import cv2
import os
from multiprocessing import Pool

# Define a function to process a single sub-image
def process_subimage(subimage):
    # Perform some image processing (e.g., convert to grayscale)
    gray = cv2.cvtColor(subimage, cv2.COLOR_BGR2GRAY)
    return gray

def process_image_with_threads(image_path, num_threads):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Determine the size of each sub_image
    height, width, _ = image.shape
    subimage_height = height // num_threads # the height dimension of sub_image
    subimage_width = width # the width remains the same

    # Split the image into sub-images based on height
    subimages = []
    for i in range(num_threads):
        y1 = i * subimage_height
        y2 = (i + 1) * subimage_height
        subimage = image[y1:y2, 0:subimage_width]
        subimages.append(subimage)

    # Process the sub-images with multiple threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Process the sub-images with multiple threads
        futures = []
        for subimage in subimages:
            future = executor.submit(process_subimage, subimage)
            futures.append(future)

        # Wait for all the futures to complete 
        # and combine the results 
        # in the same order as they were submitted
        subimages_processed = []
        for future in futures:
            subimages_processed.append(future.result())
        image_processed = np.concatenate(subimages_processed, axis=0)

    # Save the processed image
    processed_path = 'processed_' + image_path
    cv2.imwrite(processed_path, image_processed)
    print(f"Processed image saved at {processed_path}")


def process_images(image_paths, num_procs, num_threads = 4):
    with Pool(num_procs) as pool:
        results = []
        for i in image_paths:
            result = pool.apply_async(process_image_with_threads, args = (i, num_threads))
            results.append(result)
        pool.close()
        pool.join()
   
    return results

if __name__ == '__main__':
    # Define the paths to the input images and the number of threads to use
    
    # incase want to get files from a specific file
    # image_paths = ['./input/' + i for i in os.listdir("./input/")]
    
    image_paths = ['image1.jpeg', 'image2.jpeg', 'image3.jpeg']
    num_procs = 4

    # Process the images with multiple processors
    results = process_images(image_paths, num_procs)
