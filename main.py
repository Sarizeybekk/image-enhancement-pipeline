import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükleme
image = cv2.imread('input.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 1. Histogram Analizi
def plot_histogram(image, title):
    plt.figure()
    plt.hist(image.ravel(), bins=256, range=(0, 256))
    plt.title(title)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

plot_histogram(image_gray, "Orijinal Görüntü Histogramı")

# 2. Histogram Eşitleme
equalized = cv2.equalizeHist(image_gray)
plot_histogram(equalized, "Histogram Eşitleme Sonrası")

# 3. CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_equalized = clahe.apply(image_gray)
plot_histogram(clahe_equalized, "CLAHE Sonrası")

# 4. Gürültü Azaltma
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
median_blur = cv2.medianBlur(image, 5)
bilateral_filter = cv2.bilateralFilter(image, 9, 75, 75)
nlm_denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

# 5. Parlaklık ve Kontrast Ayarı
alpha = 1.5  # Kontrast faktörü
beta = 50    # Parlaklık faktörü
bright_contrast = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Görüntüleri Karşılaştırma
images = [
    ("Orijinal", image),
    ("Gaussian Blur", gaussian_blur),
    ("Median Blur", median_blur),
    ("Bilateral Filter", bilateral_filter),
    ("Non-Local Means", nlm_denoised),
    ("Bright & Contrast", bright_contrast),
]
for i, (name, img) in enumerate(images):
    plt.figure()
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(name)
    plt.axis('off')

plt.show()
