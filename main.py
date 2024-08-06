from preprocessing import preprocess_image, display_images
from localization import localize_plate, draw_bounding_box
from characterrecognition import extract_characters, recognize_characters

def main(image_path):
    image, binary_image = preprocess_image(image_path)
    display_images(image, binary_image)
    
    plate_region = localize_plate(binary_image)
    draw_bounding_box(image, plate_region)

    plate_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    char_images = extract_characters(plate_image, plate_region)
    recognized_text = recognize_characters(char_images)
    print("Recognized Text:", recognized_text)

if __name__ == "__main__":
    image_path = 'car.jpg'
    main(image_path)
