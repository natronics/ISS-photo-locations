"""Example Code to get thumbnail and larger Image URLs"""

THUMB_URL_BASE = "http://eol.jsc.nasa.gov/sseop/images/thumb/{mission}/{mrf}.jpg"
SMALL_URL_BASE = "http://eol.jsc.nasa.gov/sseop/images/ESC/small/{mission}/{mrf}.jpg"
LARGE_URL_BASE = "http://eol.jsc.nasa.gov/sseop/images/ESC/large/{mission}/{mrf}.jpg"

# Read in a CSV file
with open("../data/ISS001.csv") as f:
    for line in f:
        columns = line.split(',')
        mrf = columns[0] #mission-roll-frame
        mission = mrf.split('-')[0]

        #Thumbnail Image
        thumb_url = THUMB_URL_BASE.format(mission=mission, mrf=mrf)

        # Small Image (~640 px?)
        small_url = SMALL_URL_BASE.format(mission=mission, mrf=mrf)

        # Large Image (3000px+)
        large_url = LARGE_URL_BASE.format(mission=mission, mrf=mrf)

        # Use image URLs here (return them in a function, write them to file, etc.
        print thumb_url, small_url, large_url
