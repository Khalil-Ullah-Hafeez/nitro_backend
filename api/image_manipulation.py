def shadowDetection(img):


    return img

    # # Convert the image to grayscale
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # # Create a binary mask of the shadow using Otsu's thresholding
    # ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # # Create a copy of the original image and fill everything with red color
    # red = img.copy()
    # red[:, :, :] = [0, 0, 255]
    # red[mask == 255] = img[mask == 255]

    # # Find contours of the shadow and draw a yellow outline around it
    # contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(red, contours, -1, (0, 255, 255), 2)

    # # Save the result as a file
    # return red


def computeResult(img):
    # # In this example, img.split() returns a tuple of three individual band images, which are then saved as separate grayscale images representing the red, green, and blue channels of the original RGB image.
    # red_band, green_band, blue_band = img.split()

    # # The getdata() method of an image in the Python Imaging Library (PIL) can be used to retrieve the pixel values of an image as a flat sequence of values.
    # # getdata() method of each color band. This method returns a list of pixel values, where each value represents the intensity of the corresponding pixel in the range 0 to 255.
    # # it calculates the concentration of each color by dividing the sum of the pixel values for that color by the maximum possible value (255) times the total number of pixels in the image.
    # red_data = list(red_band.getdata())
    # green_data = list(green_band.getdata())
    # blue_data = list(blue_band.getdata())
    
    # # Calculate the concentration of each color as a number
    # total_pixels = len(red_data)
    # red_concentration = sum(red_data) / (255 * total_pixels)
    # green_concentration = sum(green_data) / (255 * total_pixels)
    # blue_concentration = sum(blue_data) / (255 * total_pixels)

    # # Processing the colors in algorithm
    
    # # M4 = R / (R+G+B)
    # M4 = red_concentration / (red_concentration + green_concentration + blue_concentration)
    
    # # M7 = R - G
    # M7 = red_concentration - green_concentration
    
    # # M10 = (R - G) / (R + G)
    # M10 = (red_concentration - green_concentration) / (red_concentration + green_concentration)

    M4 = 'test'
    M7 = 'another test'
    M10 = 'another another test'

    return { 'score_1': M4, 'score_2': M7, 'score_3': M10 }