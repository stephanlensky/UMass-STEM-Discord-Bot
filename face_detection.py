import cv2 #requires Aptfile
import numpy as np
from urllib.request import Request, urlopen
from PIL import Image
from overlay import url_to_image
import requests
from io import BytesIO

# pastes image "face" on image opened from image_path
def paste_on_face(face_path, image_url):
    # open image in opencv format and find the coordinates and dimensions of faces
    image_for_coordinates = open_image_cv(image_url)
    faces = face_coordinates(image_for_coordinates)

    #open the image and face to paste with the Image library
    image = url_to_image(image_url)
    face = Image.open(face_path)
    
    for (x, y, w, h) in faces:
        # make a copy of the face to resize
        selected_face = face.copy()

        #set face width and height
        face_width = int(w*2.2)
        face_height = int(h*2.2)

        # resizes to the size of the face in the image
        selected_face = selected_face.resize([face_width, face_height], Image.ANTIALIAS)
        
        # set x and y position with adjustments for centering
        x_pos = x-int(h/2)
        y_pos = y-int(7*h/8)

        # paste face onto the inputed image at the specified coordinates
        image.paste(selected_face, (x_pos, y_pos), selected_face)
        
    return image

# returns a list of the face coordinates and widths and heights of the faces in the inputed image
def face_coordinates(image):
    #sets the cascade file, change this for learning to identify different features
    casc_path = "haarcascade_frontalface_default.xml"

    # Create haar cascade
    face_cascade = cv2.CascadeClassifier(casc_path)

    # grayscale the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.26,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return faces

# opens the url in the form of an opencv image
def open_image_cv(url):
    #download image
    response = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))

    # convert to numpy array
    image = np.asarray(bytearray(response.read()), dtype="uint8")

    # read into opencv format
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
