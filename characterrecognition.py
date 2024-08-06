import cv2
import pytesseract
import numpy as np
from skimage import measure
import matplotlib.pyplot as plt

# Set the Tesseract path
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def extract_characters(image, plate_region):
    min_col, min_row, max_col, max_row = plate_region
    plate_image = image[min_row:max_row, min_col:max_col]

    _, thresh = cv2.threshold(plate_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    characters = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 10 and h > 10:  # Filter small contours
            char_image = plate_image[y:y+h, x:x+w]
            characters.append(char_image)
    return characters

def recognize_characters(char_images):
    recognized_text = []
    for char_img in char_images:
        char_img = cv2.threshold(char_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        char_img = cv2.resize(char_img, (100, 100), interpolation=cv2.INTER_AREA)
        text = pytesseract.image_to_string(char_img, config='--psm 10')
        recognized_text.append(text.strip())
    return recognized_text

def display_characters(char_images):
    fig, axes = plt.subplots(1, len(char_images), figsize=(20, 20))
    for ax, char_img in zip(axes, char_images):
        ax.imshow(char_img, cmap='gray')
        ax.axis('off')
    plt.show()

if __name__ == "__main__":
    image_path = 'car.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    plate_region = localize_plate(binary_image)
    char_images = extract_characters(image, plate_region)
    display_characters(char_images)
    recognized_text = recognize_characters(char_images)
    print("Recognized Text:", recognized_text)
