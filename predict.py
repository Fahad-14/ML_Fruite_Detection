import cv2
import joblib

# Function to extract features from images
def extract_features(image):
    # Here, we can use simple features like color histogram or HOG features
    # For simplicity, let's use color histograms
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

# Load trained model and mappings from joblib file
def load_model(model_path):
    clf, label_to_int, int_to_label = joblib.load(model_path)
    return clf, label_to_int, int_to_label

# Predict fruit label for a new image
def predict_fruit(image_path, model_path):
    # Load trained model and mappings
    clf, label_to_int, int_to_label = load_model(model_path)

    # Read the new image
    new_img = cv2.imread(image_path)
    if new_img is not None:
        # Extract features from the new image
        new_features = extract_features(new_img)

        # Predict the label for the new image
        predicted_label = clf.predict([new_features])[0]
        predicted_fruit = int_to_label[predicted_label]
        return predicted_fruit
    else:
        return "Invalid image path or image format."

# Path to the new image
new_image_path = input("Enter the path to the new image: ")

# Path to the trained model
model_path = 'fruit_classifier.joblib'

# Predict the fruit label for the new image
predicted_fruit = predict_fruit(new_image_path, model_path)
print("Predicted fruit:", predicted_fruit)

