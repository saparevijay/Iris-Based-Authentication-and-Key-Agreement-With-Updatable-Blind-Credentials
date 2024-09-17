import cv2
import numpy as np
import hashlib
from skimage.filters import gabor
import matplotlib.pyplot as plt

# Step 1: Load and preprocess the iris image
def preprocess_iris_image(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Perform Gaussian blur to reduce noise
    blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
    
    # Thresholding to isolate the iris (simplified, actual methods use segmentation algorithms)
    _, binary_img = cv2.threshold(blurred_img, 50, 255, cv2.THRESH_BINARY)
    
    return binary_img

# Step 2: Extract features from the preprocessed image using Gabor filters
def extract_features(image):
    # Define Gabor filter parameters (you can tune these)
    frequency = 0.6  # Adjust the frequency for the iris pattern
    theta = 0        # Orientation of the Gabor filter

    # Apply Gabor filter
    real, imag = gabor(image, frequency=frequency, theta=theta)
    
    # Combine real and imaginary parts to form the feature vector
    features = np.sqrt(real**2 + imag**2).flatten()

    # Normalize features
    normalized_features = (features - np.min(features)) / (np.max(features) - np.min(features))

    return normalized_features

# Step 3: Hash the feature vector to 256 bits using SHA-256
def hash_to_256_bits(features):
    # Convert the feature vector to a string
    feature_string = ''.join(map(str, features))
    
    # Hash the feature string using SHA-256
    sha256_hash = hashlib.sha256(feature_string.encode())
    
    # Convert the hash to a binary string (256 bits)
    hashed_binary_string = bin(int(sha256_hash.hexdigest(), 16))[2:].zfill(256)
    
    return hashed_binary_string

# Main function to process the iris image and generate a 256-bit code
def iris_image_to_256_bits(image_path):
    # Step 1: Preprocess the iris image
    preprocessed_image = preprocess_iris_image(image_path)
    
    # Step 2: Extract features from the image
    features = extract_features(preprocessed_image)
    
    # Step 3: Hash the features to get a 256-bit code
    iris_256_bit_code = hash_to_256_bits(features)
    
    return iris_256_bit_code


# iris_recognition.py

def extract_iris_code():
    
    return iris_256_bit_code


# Example usage with an iris image file
image_path = 'images\S2002R20.jpg'
iris_256_bit_code = iris_image_to_256_bits(image_path)
print("256-bit Iris Code:", iris_256_bit_code)

# Optional: Display the preprocessed image
plt.imshow(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE), cmap='gray')
plt.title('Preprocessed Iris Image')
plt.show()
