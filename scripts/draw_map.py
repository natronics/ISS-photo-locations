""" Draw a map of all the data points in the data folder. Requires python-cairo"""
import cairo

# Width and Height of the output image
width = 3600 #px
height = 1800 #px


# Define the mapping from lat/lon to x,y in pixels:
# compute the conversion factors (pay attention in linear algibra, kids)
lata = -height / 180.0
latb = height - (lata*-90.0)
lona = width / 360.0
lonb = lona*180.0

# X screen coord helper
def x(l):
    return (lona*l) + lonb
# Y screen coord helper
def y(l):
    return (lata*l) + latb


# Create an image surface and context
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
cr = cairo.Context(surface)

# Draw a solid rectangle as the background
cr.set_source_rgb(1, 1, 1) #white
cr.rectangle(0, 0, width, height)
cr.fill()

# Loop through all the missions
for m in xrange(1,35):
    print "drawing mission", m
    # Open file
    with open("../data/ISS%03d.csv" % m, 'r') as f:
        # Read lines
        for line in f:
            # Get lat, lon
            columns = line.split(',')
            lat = float(columns[1])
            lon = float(columns[2])

            # Draw a dark pixel at the image coordinate
            cr.set_source_rgba(0, 0, 0, 0.2) #black, at 20% opacity
            cr.rectangle(x(lon), y(lat), 1, 1)
            cr.fill()

# Write out image to disk
surface.write_to_png("ISS_photos.png")

""" Notes:
On my desktop (linux, 3.0 GHz processor):
    $ time python draw_map.py
    drawing mission 1
    drawing mission 2
    ...
    drawing mission 34

    real    0m6.179s
    user    0m6.128s
    sys     0m0.040s

Draws all 1.1 million points in less than six and a half seconds!
"""
