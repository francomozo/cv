import cv2

# Load the image
image = cv2.imread("img.jpeg")

# Calculate the new dimensions of the image (half the original size)
new_width = image.shape[1] // 2
new_height = image.shape[0] // 2

# Resize the image using cv2.resize()
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image
cv2.imwrite("resized_image.jpg", resized_image)
