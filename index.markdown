---
layout: article
title: ISS photos
---

# Location of Every Photo From the ISS

<span class="pubdate">March 2013</span>

 Since the first mission to the International Space Station over 12 years ago
there have been over a _million_ photographs taken by astronauts looking out
from four hundred kilometers above Earth. Nearly all of them have been
[archived on NASA's servers]("http://eol.jsc.nasa.gov/). I've crawled that
archive, pulling down the location for each of the 1,129,177 photographs taken
from the ISS<sup>1</sup>. <span class="footnote"><sup>1</sup>Photos were only
archived if they were found in the database and had a known latitude and
longitude. It's not necessarily every single image ever taken, but it's close.</span>


### The Data

Downloads:

 - [.zip](https://github.com/natronics/ISS-photo-locations/archive/master.zip)
 - [.tar.gz](https://github.com/natronics/ISS-photo-locations/archive/master.tar.gz)
 - [View on github](https://github.com/natronics/ISS-photo-locations/)


### Files

The data exists in a collection of .csv files in the folder `data`. There is a
file for each ISS mission, `ISS001.csv`, `ISS002.csv`, etc. in the following format:

<table class="table table-striped">
 <tbody>
  <tr><th>Column</th><td>Mission Roll Frame</td><td>Latitude</td><td>Longitude</td></tr>
  <tr><th>Example</th><td>ISS001-E-5411,</td><td>45.5,</td><td>-122.6</td></tr>
 </tbody>
</table>


## Visualization

If we draw a dot for the location of every photo of Earth taken from space
what do we see?

<div class="image primary">
  <a href="visualizations/all_iss.png" onClick="_gaq.push(['_trackEvent', 'Photos', 'fullsize', 'All missions']);">
    <img class="img-responsive" src="visualizations/all_iss.preview.png" alt="Dot for very ISS image">
  </a>
</div>

Most of the photos are taken of land. Coastlines, islands and cities seem
to be popular targets. So much so that it's possible to make out basic
continents. This makes sense, photos of clouds over an otherwise blank ocean
get old after a while. I'm sure every astronaut has taken at least one
photograph of the town they grew up in.

Now let's divide up the dots by mission. Is there any pattern? Here each mission
is shown in a different color:

<div class="image primary">
  <a href="visualizations/all_iss_missions.png" onClick="_gaq.push(['_trackEvent', 'Photos', 'fullsize', 'All missions colored']);">
    <img class="img-responsive" src="visualizations/all_iss_missions.preview.png" alt="Dot for very ISS image with colors for each mission">
  </a>
</div>

The map is dominated by purple, light blue, and green with some yellow<sup>2</sup>.
<span class="footnote"><sup>2</sup>ISS 30/31, 22, 13, and 6 respectively</span> I
also notice that the purple dots make almost uninterrupted orbit lines while most
of the other dots seem to fill in randomly. This is because during ISS 30/31
[Don Pettit took dozens of amazing time lapse sequences](http://vimeo.com/61083440)
consisting of hundreds of images taken continuously as the ISS orbited. In fact
he's single-handedly responsible for almost half the images taken on orbit!
Here's the breakdown:


### Photo count by mission

{% include barchart.html %}

One more thing we can do is add a map underneath to see exactly how the photos line up:

<div class="image primary">
  <a href="visualizations/all_iss_missions_map.png"  onClick="_gaq.push(['_trackEvent', 'Photos', 'fullsize', 'All missions colored with map']);">
    <img class="img-responsive" src="visualizations/all_iss_missions_map.preview.png" alt="dot for every image, colored by mission, with map underlay">
  </a>
</div>

Here you can see that the ISS stays between about 50&deg; and -50&deg; latitude as it orbits the Earth
The [inclination](http://en.wikipedia.org/wiki/Orbital_inclination) of the orbit
of the station is in fact 51.6&deg;. This is high enough that it can communicate
with ground stations in Russia, while low enough that vehicles launching from the USA
can reach it.

Since it's hard to see the overlapped colors in the above image here is a
collection maps with the photos from each mission mapped separately:

<div class="image primary">
  <a href="visualizations/small_mult.png" onClick="_gaq.push(['_trackEvent', 'Photos', 'fullsize', 'Small multiples']);">
    <img class="img-responsive" src="visualizations/small_mult.preview.png" alt="collection maps with the photos from each mission mapped sepretely">
  </a>
</div>

The sudden explosion during ISS 30 is really evident here. And it looks like time
lapses started becoming popular around ISS 28.

This is just some of the data that NASA has to offer. If you're interested in getting
involved in things like this I suggest taking a look at
[data.nasa.gov](http://data.nasa.gov/),
[International Space Apps Challenges](http://spaceappschallenge.org/),
[spacehack.org](http://spacehack.org/) and of course, downloading this dataset.

Because this data is from NASA it is in the public domain. If you do end up using it
I'd be interested in hearing about it. Feel free to [drop me a line](http://natronics.github.com/aboutme)
if you end up making something with it.

{% include share.html %}
