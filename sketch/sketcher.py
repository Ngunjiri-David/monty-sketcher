# OpenCV and matplotlib are the 
# only libraries needed.
import cv2
import matplotlib.pyplot as plt

# Read the image from source then
# store it in the img variable:
img = cv2.imread("y:/projects/open_source/sketch/arctic_wolf.jpg")

# Displaying the original image:
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Using the matplotlib-pyplot module
# to get around the hassles of displaying
# the image. Displayed in jupyter notebook.
plt.imshow(img)
plt.axis(False)
plt.show()

# The plotted image is in the RGB color scheme
# while the cv2 image is in BGR.
# 2 conversion methods can be used:
# 1:
# plt.imshow(img[:,:,::-1])
# plt.axis(False)
# plt.show()

# 2: using cvtColor method of openCV
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.axis(False)
plt.show()

# Sketch
# 1: Gray image:
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2: Invert image:
# Either:
#invert_img = cv2.bitwise_not(gray_img)
# Or:
invert_img = 255-gray_img

# 3: Apply Gaussian blur to the image:
# The second argument of the function is the kernel size,
# a pair of odd numbers. Direct proportion between kernel size
# and level of blur.
blur_img = cv2.GaussianBlur(invert_img, (99,99),0)
plt.imshow(blur_img)
plt.axis(False)
plt.show()

# 4: Invert blurred image:
invblur_img = cv2.bitwise_not(blur_img)

# 5: Sketch:
sketch_img = cv2.divide(gray_img, invblur_img, scale = 256.0)

# 6: Save the Sketch:
cv2.imwrite('sketch.png', sketch_img)

# 7: Display the sketch:
cv2.imshow('sketch image', sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# You can display the original image and the sketch
# side-by-side for comparison:
plt.figure(figsize = (14,8))

plt.subplot(1, 2, 1)
plt.title('Original image', size = 18)
plt.imshow(rgb_img)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Sketch', size = 18)
rgb_sketch = cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_sketch)
plt.axis('off')
plt.show()


# You can put everything together to create
# a sketch function.
