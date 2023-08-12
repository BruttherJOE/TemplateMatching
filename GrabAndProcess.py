import numpy as np
from PIL import ImageGrab
import cv2

# Capture the entire screen
screenshot = ImageGrab.grab()
template = cv2.imread("C:\\Users\\brutt\\Desktop\\code\\TemplateMatching\\res\\testMoo.png")

# Convert Pillow image to a NumPy array
screenshot_np = np.array(screenshot)

# Convert RGB to BGR (OpenCV uses BGR color order)
screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

# Convert both images to grayscale
screenshot_gray = cv2.cvtColor(screenshot_bgr, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Check if the template is found
threshold = 0.8  # Adjust this threshold as needed
if max_val >= threshold:
    # Extract the location of the detected object
    top_left = max_loc
    h, w = template_gray.shape
    bottom_right = (top_left[0] + w, top_left[1] + h) # 0 = xval, 1 = yval

    # Draw a green rectangle around the detected object
    cv2.rectangle(screenshot_bgr, top_left, bottom_right, (0, 255, 0), 2)

    # Calculate percentage match
    percentage_match = round(max_val * 100, 2)

    # Add the percentage match to the displayed result
    text = f"Percentage Match: {percentage_match}%"
    cv2.putText(screenshot_bgr, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Detection Result", screenshot_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Template not found in the provided image.")
