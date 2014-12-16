# Installation

None

# How to use

Run:

    python server.py

Visit http://localhost:5000/

## Usage:

Most usage should be self-explanatory.  Select an image, and draw over the image.
As you draw, paths show up in the right hand select list.

You can select 1 or multiple paths.  When 1 path is selected, you can adjust the
times it covers.  By default, the timestamps are recoded when you draw a path
and will be streched to go between 0 to 600 seconds.  So a 6 seconds stroke will
be slowed down 100x.

You can import and export to json files as well.


## BLTR:

Load a map image - this can be any jpeg.  You can also select a bounds json
file (not really used yet).  The file should look like:

    {
        "bl": [0, 0],
        "tr": [600, 800]
    }

The points will scale linearly so the bottom left and top right match these
coordinates.


