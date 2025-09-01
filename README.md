# 📸 Image Processing App

A powerful web-based image processing application built with Streamlit and OpenCV that allows users to apply various computer vision techniques to their images through an intuitive interface.

## Features

### Core Image Processing Operations
- **Face Detection**: Automatically detect and highlight faces using Haar Cascade classifiers
- **Edge Detection**: Apply Canny edge detection to identify object boundaries
- **Grayscale Conversion**: Convert color images to grayscale
- **Gaussian Blur**: Apply blur effects with customizable intensity
- **Binary Thresholding**: Convert images to binary (black and white) format
- **Contour Detection**: Identify and highlight object contours
- **Image Sharpening**: Enhance image clarity and details
- **Emboss Effect**: Create artistic embossed appearance
- **Cartoonization**: Transform photos into cartoon-style images
- **Color Inversion**: Create negative image effects

### User Experience
- **Drag & Drop Upload**: Easy image upload interface supporting JPG, PNG, and JPEG formats
- **Real-time Processing**: Instant image processing with visual feedback
- **Download Functionality**: Save processed images directly to your device
- **Responsive Design**: Optimized layout for both desktop and mobile devices
- **Interactive Sidebar**: Intuitive controls for operation selection and settings

## Demo

*Add screenshots or GIFs of your application in action*

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/image-processing-app.git
cd image-processing-app
```

2. **Install dependencies:**
```bash
pip install streamlit opencv-python pillow numpy plotly
```

3. **Run the application:**
```bash
streamlit run app.py
```

4. **Access the app:** Open your browser and go to `http://localhost:8501`

### Alternative Installation with requirements.txt

Create a `requirements.txt` file with:
```
streamlit>=1.28.0
opencv-python>=4.8.0
Pillow>=10.0.0
numpy>=1.24.0
plotly>=5.15.0
```

Then install with:
```bash
pip install -r requirements.txt
```

## Usage Guide

### Step-by-Step Instructions

1. **Upload an Image**
   - Click "Browse files" in the sidebar
   - Select an image file (JPG, PNG, or JPEG)
   - The image will be automatically loaded

2. **Choose Processing Operation**
   - Select from 11 different processing techniques in the dropdown menu
   - Each operation applies different computer vision algorithms

3. **Apply Processing**
   - Click the "Apply" button to process your image
   - Wait for the processing indicator to complete

4. **Download Results**
   - Once processed, use the "Download Processed Image" button
   - The processed image will be saved as a PNG file

### Processing Operations Explained

| Operation | Description | Use Case |
|-----------|-------------|----------|
| **Original** | Display unmodified image | Comparison baseline |
| **Face Detection** | Detect and highlight human faces | Security, photo organization |
| **Edge Detection** | Highlight object boundaries | Object recognition, analysis |
| **Grayscale** | Convert to black and white | Artistic effects, preprocessing |
| **Blur** | Apply Gaussian blur filter | Privacy, artistic effects |
| **Thresholding** | Convert to binary image | Document processing, analysis |
| **Contour Detection** | Identify object outlines | Shape analysis, measurement |
| **Sharpen** | Enhance image clarity | Photo enhancement |
| **Emboss** | Create 3D embossed effect | Artistic processing |
| **Cartoonize** | Cartoon-style transformation | Creative effects |
| **Invert** | Create negative image | Artistic effects, analysis |

## Technical Architecture

### Dependencies
- **Streamlit**: Web application framework for the user interface
- **OpenCV (cv2)**: Computer vision library for image processing algorithms
- **NumPy**: Numerical computing for array operations
- **Pillow (PIL)**: Image handling and format conversion
- **Plotly**: Visualization library (inherited from base template)

### Key Functions
- `load_image()`: Handles image upload and conversion to NumPy arrays
- `convert_bgr_to_rgb()`: Fixes color channel ordering for proper display
- `process_image()`: Main processing dispatcher using operation mapping
- Individual processing functions for each computer vision technique

### Data Flow
1. User uploads image → PIL Image object
2. Convert to NumPy array → OpenCV processing
3. Apply selected operation → Color space correction
4. Display result → Optional download

## Project Structure

```
image-processing-app/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # License file (optional)
└── assets/               # Screenshots and demo images (optional)
    ├── demo_original.jpg
    ├── demo_processed.jpg
    └── app_screenshot.png
```

## Advanced Features

### Session State Management
The app uses Streamlit's session state to maintain processed images across interactions, enabling seamless download functionality.

### Error Handling
- Robust file format validation
- Graceful handling of processing errors
- User-friendly error messages

### Performance Optimizations
- Efficient memory management with image copying
- Optimized OpenCV operations
- Responsive UI with processing indicators

## Deployment

### Local Development
```bash
streamlit run app.py
```

### Cloud Deployment Options
- **Streamlit Cloud**: Connect your GitHub repository for automatic deployment
- **Heroku**: Deploy using the Heroku CLI with a `Procfile`
- **Docker**: Containerize the application for consistent deployment

### Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Add new processing operations or improve existing ones
4. **Test thoroughly**: Ensure all operations work with various image types
5. **Commit changes**: `git commit -m 'Add amazing feature'`
6. **Push to branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Contribution Ideas
- Add new image processing operations
- Improve error handling
- Add batch processing capabilities
- Implement image format conversions
- Add image metadata display

## Troubleshooting

### Common Issues

**Issue**: "No module named 'cv2'"
**Solution**: Install OpenCV with `pip install opencv-python`

**Issue**: Images appear with wrong colors
**Solution**: The app automatically handles BGR to RGB conversion

**Issue**: Face detection not working
**Solution**: Ensure uploaded images contain clear, front-facing faces

### System Requirements
- **RAM**: Minimum 4GB (8GB recommended for large images)
- **Storage**: 100MB free space for dependencies
- **Internet**: Required for initial package installation



## Acknowledgments

- **OpenCV Community** for the computer vision algorithms
- **Streamlit Team** for the excellent web framework
- **Haar Cascade Classifiers** for face detection models
- **PIL/Pillow** for image handling capabilities

## Support & Contact

- **Issues**: [GitHub Issues](https://github.com/yourusername/image-processing-app/issues)
- **Documentation**: [OpenCV Documentation](https://docs.opencv.org/)

## Roadmap

### Version 2.0 Planned Features
- [ ] Batch image processing
- [ ] Custom filter creation
- [ ] Image format conversion tools
- [ ] Advanced face recognition
- [ ] Object detection and classification
- [ ] Image enhancement algorithms
- [ ] Histogram analysis and equalization
- [ ] Morphological operations
- [ ] Color space transformations
- [ ] Image segmentation tools

---

**Transform your images with professional computer vision techniques!** 🎨🔍
