import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Load image and convert it to a NumPy array
def load_image(image_file):
    image = Image.open(image_file)
    return np.array(image)

# Convert BGR to RGB (Fix for blue tint)
def convert_bgr_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Face detection function
def face_detection(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return convert_bgr_to_rgb(image)  # Ensure correct color format

# Edge detection function
def edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

# Convert image to grayscale
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
def blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)

# Apply binary thresholding
def threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return thresh

# Contour detection
def contour_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    return convert_bgr_to_rgb(image)  # Ensure correct color format

# Sharpen the image
def sharpen(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return convert_bgr_to_rgb(cv2.filter2D(image, -1, kernel))

# Apply an emboss effect
def emboss(image):
    kernel = np.array([[ -2, -1, 0], [-1, 1, 1], [0, 1, 2]])
    return convert_bgr_to_rgb(cv2.filter2D(image, -1, kernel))

# Apply a cartoon effect
def cartoonize(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    color = cv2.bilateralFilter(image, 9, 300, 300)  # Smoothen colors
    cartoon_image = cv2.bitwise_and(color, color, mask=edges)
    return convert_bgr_to_rgb(cartoon_image)

# Invert colors of the image
def invert(image):
    return convert_bgr_to_rgb(cv2.bitwise_not(image))

# Process image based on user selection
def process_image(image, operation):
    operations = {
        "Original": lambda img: img,
        "Face Detection": face_detection,
        "Edge Detection": edge_detection,
        "Grayscale": grayscale,
        "Blur": blur,
        "Thresholding": threshold,
        "Contour Detection": contour_detection,
        "Sharpen": sharpen,
        "Emboss": emboss,
        "Cartoonize": cartoonize,
        "Invert": invert
    }
    
    return operations.get(operation, lambda img: img)(image.copy())

# Main function for the Streamlit app
def main():
    st.set_page_config(page_title="Image Processing App", page_icon="📷", layout="wide")

    st.title("📸 Image Processing App")
    st.write("Upload an image and apply various image processing techniques!")

    with st.sidebar:
        st.header("🔧 Settings")
        uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

        # Select an operation
        operation = st.selectbox("Choose an Operation", [
            "Original", "Face Detection", "Edge Detection", "Grayscale", "Blur",
            "Thresholding", "Contour Detection", "Sharpen", "Emboss", "Cartoonize", "Invert"
        ])

        # Ensure an image is uploaded before processing
        if uploaded_file:
            image = load_image(uploaded_file)
            
            if st.button("Apply"):
                with st.spinner("Processing..."):
                    processed_image = process_image(image, operation)
                    st.session_state["processed_image"] = processed_image  # Store in session state

                # Display processed image
                st.image(processed_image, caption=f"Processed Image ({operation})", use_column_width=True)

            # Enable download button after processing
            if "processed_image" in st.session_state:
                st.download_button(
                    label="💾 Download Processed Image",
                    data=cv2.imencode('.png', st.session_state["processed_image"])[1].tobytes(),
                    file_name="processed_image.png",
                    mime="image/png"
                )

# Run the app
if __name__ == "__main__":
    main()
