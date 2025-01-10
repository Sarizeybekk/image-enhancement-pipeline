# Image Enhancement and Optimization

This project focuses on enhancing image quality through brightness and contrast optimization, noise reduction, and other image processing techniques. The purpose is to improve the visual quality of images for better analysis and usability.

---

## Features
- **Histogram Equalization**: Global contrast improvement.
- **CLAHE (Contrast Limited Adaptive Histogram Equalization)**: Local contrast enhancement while avoiding over-saturation.
- **Noise Reduction**:
  - Gaussian Blur
  - Median Filter
  - Bilateral Filter
  - Non-Local Means Filter
- **Brightness & Contrast Adjustment**: Fine-tune image appearance using linear transformations.
- **Pipeline Visualization**: A consolidated view of all processing steps.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/image-enhancement.git
   cd image-enhancement
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Requirements

- Python 3.7 or above
- Required Python packages (listed in `requirements.txt`):
  - `numpy`
  - `opencv-python`
  - `matplotlib`

---

## Usage

1. Place your input image in the root directory of the project and rename it as `input_image.jpg`.
2. Run the main script to execute the image processing pipeline:
   ```bash
   python main.py
   ```
3. The output will be displayed as a visual comparison of all processing steps in a single matplotlib window.

---

## Output

The script provides the following outputs:
1. **Original Image**
2. **Histogram Equalization Result**
3. **CLAHE Result**
4. **Gaussian Blur**
5. **Median Blur**
6. **Bilateral Filter**
7. **Non-Local Means Filter**
8. **Brightness & Contrast Adjustment**

All outputs are visualized in a single window for easy comparison.

---

## Suggested Test Images
- Low-light or dark images.
- High-noise images (e.g., old scanned photos or low-resolution images).
- Natural landscapes or cityscapes with diverse lighting conditions.

---

## Future Enhancements
- **Deep Learning Integration**: Add super-resolution and advanced denoising methods using pretrained models.
- **GUI Application**: Develop a user-friendly graphical interface.
- **Batch Processing**: Enable processing of multiple images simultaneously.

---



---

## Acknowledgments
This project uses:
- OpenCV for image processing.
- NumPy for numerical operations.
- Matplotlib for visualization.

---


<img width="602" alt="Ekran Resmi 2025-01-10 21 32 22" src="https://github.com/user-attachments/assets/b48f3d9e-eb97-49e4-aeb3-3eadf3cfabd7" />
<img width="605" alt="Ekran Resmi 2025-01-10 21 32 47" src="https://github.com/user-attachments/assets/d31f0c45-2df9-4df8-8979-c2558b452e7f" />
<img width="598" alt="Ekran Resmi 2025-01-10 21 32 39" src="https://github.com/user-attachments/assets/ca686d91-6ab8-4025-9ae2-5ada636e87da" />
<img width="612" alt="Ekran Resmi 2025-01-10 21 31 32" src="https://github.com/user-attachments/assets/ffd168d7-3744-45e1-97e3-429d6895726f" />
<img width="589" alt="Ekran Resmi 2025-01-10 21 32 05" src="https://github.com/user-attachments/assets/46b163c9-b591-459f-acb8-c18938bfc973" />

