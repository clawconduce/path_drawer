# Installation

None

# How to use

Run:

    python server.py

Visit http://localhost:5000/

Load a map image - this can be any jpeg.  You can also select a bounds json
file (not really used yet).  The file should look like:

    {
        "bl": [0, 0],
        "tr": [600, 800]
    }

The points will scale linearly so the bottom left and top right match these
coordinates.

