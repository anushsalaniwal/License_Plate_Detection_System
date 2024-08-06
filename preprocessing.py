import cv2
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    threshold_value = threshold_otsu(blurred_image)
    binary_image = blurred_image > threshold_value
    return image, binary_image

def display_images(original, processed):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.imshow(original, cmap='gray')
    ax1.set_title('Original Image')
    ax2.imshow(processed, cmap='gray')
    ax2.set_title('Processed Image')
    plt.show()

if __name__ == "__main__":
    image_path = 'car.jpg'
    image, binary_image = preprocess_image(image_path)
    display_images(image, binary_image)
    