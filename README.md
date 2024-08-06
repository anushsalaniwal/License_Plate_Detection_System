# License_Plate_Detection_System

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/license-plate-recognition.git
    cd license-plate-recognition
    ```

2. **Set up a virtual environment:**

    ```sh
    pip install virtualenv
    virtualenv lpr
    ```

3. **Activate the virtual environment:**

    - On macOS/Linux:
        ```sh
        source lpr/bin/activate
        ```
        
4. **Install the required packages:**

    ```sh
    pip install opencv-python pytesseract numpy matplotlib scikit-image
    ```

5. **Ensure Tesseract-OCR is installed:**

    - On macOS using Homebrew:
        ```sh
        brew install tesseract
        ```

6. **Run the main script:**

    ```sh
    python main.py
    ```

## Project Structure

- `preprocessing.py`: Contains image preprocessing functions.
- `localization.py`: Contains license plate localization functions.
- `characterrecognition.py`: Contains character extraction and recognition functions.
- `main.py`: Main script to run the LPR system.
- `car.jpg`: Sample image for testing.
- `README.md`: Project documentation.

## Modules

### preprocessing.py
- **preprocess_image(image_path):** Reads and preprocesses the image.
- **display_images(original, processed):** Displays the original and processed images side by side.

### localization.py
- **localize_plate(binary_image):** Localizes the license plate in the binary image.
- **draw_bounding_box(image, plate_region):** Draws a bounding box around the localized plate region.

### characterrecognition.py
- **extract_characters(image, plate_region):** Extracts individual characters from the localized plate region.
- **recognize_characters(char_images):** Recognizes characters using pytesseract.
- **display_characters(char_images):** Displays the extracted character images.

### main.py
- **main(image_path):** Orchestrates the overall LPR process by calling functions from other modules.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenCV](https://opencv.org/)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [scikit-image](https://scikit-image.org/)
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
