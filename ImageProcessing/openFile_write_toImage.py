import matplotlib.pyplot as plt
from scipy import misc

f=misc.imread('C:/Users/User/Desktop/Machine_learning/ImageProcessing/Images/mountain.png')


# def rgb2gray(rgb):

#     r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
#     gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

#     return gray
# f = rgb2gray(f)
# #display image using matplotlib.pyplot
# plt.imshow(f)
# plt.show()

# #type of object (image)
# print(type(f))
# # shape and type of object(image)
# print(f.shape, f.dtype)

##Using sci-kit image to convert to grayscale
# import matplotlib.pyplot as plt
# from skimage import color
# from skimage import io

# img = color.rgb2gray(io.imread('C:/Users/User/Desktop/Machine_learning/ImageProcessing/Images/mountain.png'))
# plt.imshow(img)
# plt.show()



# img = io.imread('C:/Users/User/Desktop/Machine_learning/ImageProcessing/Images/mountain.png', as_gray=True)
# plt.imshow(img)
# plt.show()
























# #using OpenCV
# import cv2
  
# image = cv2.imread('C:/Users/User/Desktop/Machine_learning/ImageProcessing/Images/mountain.png')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# cv2.imshow('Original image',image)
# cv2.imshow('Gray image', gray)
  
# cv2.waitKey(0)
# cv2.destroyAllWindows()