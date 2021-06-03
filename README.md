# Movie_Barcode

Movie Barcode is a program written by me, Callum, that produces 'barcodes' of the average colour of individual frames from media files. This was made after seeing multiple posts on _reddit_ about this [link](https://www.reddit.com/r/todayilearned/comments/c813s7/til_about_movie_barcodes_which_is_when_every/).

## Prerequisites

- [OpenCV](https://pypi.org/project/opencv-python/)
- [NumPy](https://pypi.org/project/numpy/)
- [Python Image Library](https://pythonware.com/products/pil/)

## Usage

`python movie_barcode.py input_file font_file`

- Such as:

`python movie_barcode.py "Big Buck Bunny.mov" adventpro.ttf`

## Tips

- Typically, I have used [adventpro.ttf](https://www.1001fonts.com/advent-pro-font.html) with this program. It is known to scale well and appear visually appealing.
- I have tested this exclusively with [bigbuckbunny.mov](https://peach.blender.org/), it should scale to all other length of video files. Thanks to the Blender Foundation for the use of this.
- It processes frame by frame, so having a couple mb free in the working directory is definitely a requirement.

## Detailed Information

Movie 'barcodes' have been known about for a long time, the process for these programmatically is quite simple. First we capture the first frame, we extract the average colour (I know I used color/colour interchangeably, _shhh_) of this and then add it to a large array. We will do this at increments of the media file framerate, then once finished we use the Python Image Library to draw lines of 1 pixel width and fill it with this with the colour in of array.
There is much more to say, by one can understand most of it by reading the comments, and to conclude I would like to demonstrate the output of the program on Big Buck Bunny:

![an example image](https://github.com/groegercesg/Movie_Barcode/blob/master/samples/BigBuckBunny-barcode.png)

## Known Issues

- Has to process frame by frame (sequentially), potentially slow for large files. Concurrency could potentially be used to help.

## Desired Features

- Use a vignette on the top and bottom of the barcode section to make the output more visually appealing
