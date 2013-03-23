# ISS-photo-locations

A data dump of the location of all photos taken from the International Space Station.

Since the first mission to the International Space Station over 12 years ago there
have been over a million of photographs taken by astronauts from their perch four
hundred kilometers above Earth. Nearly all of them have been archived on NASA’s
servers. I've crawled that archive and pulled out the approximate location of the
ISS when each photo was taken.

## Format

The data exists in a collection of .csv files in the folder `./data/`. There is a
file for each ISS mission, `ISS001.csv`, `ISS002.csv`, etc. in the following format:

    Column   Mission-Roll-Frame | Latitude | Longitude
    Example  ISS001-E-5411, 45.5, -122.6

## Example Use

In python you could read in a file like this:

```python
with open("data/ISS001.csv") as f:
    for line in f:
        columns = line.split(',')
        mrf = columns[0]
        latitude = float(columns[1])
        longitude = float(columns[2])
        print mrf, latitude, longitude
```

## License

This dataset is courtisy of the
[Image Science and Analysis Laboratory, NASA-Johnson Space Center. http://eol.jsc.nasa.gov/](http://eol.jsc.nasa.gov/)

NASA still images; audio files; video; and computer files used in the rendition of 3-dimensional
models, such as texture maps and polygon data in any format, generally are not copyrighted.
You may use NASA imagery, video, audio, and data files used for the rendition of 3-dimensional
models for educational or informational purposes, including photo collections, textbooks, public
exhibits, computer graphical simulations and Internet Web pages. This general permission
extends to personal Web pages.

The accompanying articles and visualizations are copyrighted by Nathan Bergey and available under a Creative Commons Attribution 3.0 License.
