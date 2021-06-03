###
# Program Name: movie_barcode.py
# Program Function: Take a video file as input and from that
# create a 'barcode' style image of the average colour for each
# frame.
# Program Author: Callum Groeger
###

# import modules
import cv2
import numpy
import os
import sys
from base64 import b16encode
from PIL import Image, ImageDraw, ImageFont

file_name = str(sys.argv[1])

# set required variables and find FPS
vidcap = cv2.VideoCapture(file_name)
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))
frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
# divide but without remainders
duration = (frame_count // fps)
hexes = [None] * (duration+1)
array_fill = 0

# loop through every frame in video file

while success:
    # read in image from videocapture
    success, image = vidcap.read()

    # if count MOD fps given 0, i.e. count divided by fps has no remainders
    # (fps = 24, count = 0, 24, 48...)
    # if this is the case then begin process
    if count % (fps) == 0:

        # set filename, used for deletion late
        filename = 'frame%d.jpg' % count

        # write out image
        cv2.imwrite(filename, image)

        # read in image
        myimg = cv2.imread(filename)

        # find average colour, returned in BGR format
        # which is useful as cv2 reads an image in BGR format
        avg_color_per_row = numpy.average(myimg, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
        avg_color = str(avg_color)

        # turn BGR colour into RGB:

        def bgr_hex(bgr):
            # strip starting square brackets
            strip_bgr = str(bgr)[1:-1]
            # split on spaces
            splitted = strip_bgr.split()
            # stick into RGB form
            rgb = [int(float(splitted[2])), int(float(splitted[1])),
                   int(float(splitted[0]))]
            # base64 encode into hex, and strip format info: b'...'
            rgb = str(b16encode(bytes(rgb)))[2:-1]
            return rgb

        hexes[array_fill] = bgr_hex(avg_color)
        array_fill += 1

        # remove file
        os.remove(filename)
    # increment count to continue process
    count += 1

# code for creating the image

# width and height of image, height=480 which is just a standard size
# that I have arbitrarily determined
W, H = (len(hexes), 480)

# make a new image with prior determined dimensions
im = Image.new('RGB', (W, H))

# setup drawing on the image
draw = ImageDraw.Draw(im)

# draw lines for all the colours
for i in range(0, len(hexes)):

    # get colour to draw from array
    COLOR = "#" + str(hexes[i])

    # draw line, incrementing x position based on i
    draw.line([i, 120, i, 480], width=1, fill=COLOR)
next

# set font defaults, this shouldn't really change
font = ImageFont.truetype(str(sys.argv[2]), 48)

# find w,h for drawing text of this particular size
w, h = draw.textsize(file_name.split('.', 1)[0], font=font)
# draw text, using estimated and default positions to dynamically
# locate central positioning
draw.text(((W-w)/2, ((H-360)-h)/2), str(file_name)[:-4],
          (255, 255, 255), font=font)

# file_path for output
file_path = file_name.split('.', 1)[0] + "-barcode.png"
im.save(file_path)
