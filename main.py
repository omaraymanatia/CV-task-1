import cv2
import numpy as np

image_path = "test.jpg"
image = cv2.imread(image_path)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

kernel = np.ones((5, 5), np.uint8)
dilated_mask = cv2.dilate(mask, kernel, iterations=1)

result = cv2.bitwise_and(image, image, mask=dilated_mask)

cv2.imwrite("Extracted.jpg", result)

cv2.imshow("Original Image", image)
cv2.imshow("Extracted Blue Circle", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
