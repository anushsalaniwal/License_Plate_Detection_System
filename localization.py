from skimage.measure import label, regionprops
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import cv2

def localize_plate(binary_image):
    labeled_image = label(binary_image)
    plate_region = None

    for region in regionprops(labeled_image):
        if region.area > 500:  # Area threshold for license plate
            min_row, min_col, max_row, max_col = region.bbox
            plate_region = (min_col, min_row, max_col, max_row)
            break

    return plate_region

def draw_bounding_box(image, plate_region):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.imshow(image, cmap='gray')
    if plate_region:
        min_col, min_row, max_col, max_row = plate_region
        rect = patches.Rectangle((min_col, min_row), max_col - min_col, max_row - min_row,
                                 edgecolor='red', linewidth=2, fill=False)
        ax.add_patch(rect)
    plt.show()

if __name__ == "__main__":
    image_path = 'car.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary_image = preprocess_image(image_path)
    plate_region = localize_plate(binary_image)
    draw_bounding_box(image, plate_region)
