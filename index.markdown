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

Most of the photos are taken of land. Coastlines, islands and cities seem
to be popular targets. So much so that it's possible to make out basic
continents. This makes sense, photos of clouds over an otherwise blank ocean
get old after a while. I'm sure every astronaut has taken at least one
photograph of the town they grew up in.

Now let's divide up the dots by mission. Is there any pattern? Here each mission
is shown in a different color:


The map is dominated by purple, light blue, and green with some yellow<sup>2</sup>.
<span class="footnote"><sup>2</sup>ISS 30/31, 22, 13, and 6 respectively</span> I
also notice that the purple dots make almost uninterrupted orbit lines while most
of the other dots seem to fill in randomly. This is because during ISS 30/31
[Don Pettit took dozens of amazing time lapse sequences](http://vimeo.com/61083440)
consisting of hundreds of images taken continuously as the ISS orbited. In fact
he's single-handedly responsible for almost half the images taken on orbit!
Here's the breakdown:


### Photo count by mission

<ul class="barchart">
 <li><span class="title">ISS001</span><span class="bar" style="width:0px;">&nbsp;</span><span class="number outside">474</span></li>
 <li><span class="title">ISS002</span><span class="bar" style="width:5px;">&nbsp;</span><span class="number outside">2,976</span></li>
 <li><span class="title">ISS003</span><span class="bar" style="width:1px;">&nbsp;</span><span class="number outside">930</span></li>
 <li><span class="title">ISS004</span><span class="bar" style="width:10px;">&nbsp;</span><span class="number outside">5,832</span></li>
 <li><span class="title">ISS005</span><span class="bar" style="width:25px;">&nbsp;</span><span class="number outside">13,801</span></li>
 <li><span class="title">ISS006</span><span class="bar" style="width:81px;">&nbsp;</span><span class="number outside">43,436</span></li>
 <li><span class="title">ISS007</span><span class="bar" style="width:21px;">&nbsp;</span><span class="number outside">11,204</span></li>
 <li><span class="title">ISS008</span><span class="bar" style="width:27px;">&nbsp;</span><span class="number outside">14,875</span></li>
 <li><span class="title">ISS009</span><span class="bar" style="width:39px;">&nbsp;</span><span class="number outside">21,259</span></li>
 <li><span class="title">ISS010</span><span class="bar" style="width:40px;">&nbsp;</span><span class="number outside">21,473</span></li>
 <li><span class="title">ISS011</span><span class="bar" style="width:15px;">&nbsp;</span><span class="number outside">8,516</span></li>
 <li><span class="title">ISS012</span><span class="bar" style="width:29px;">&nbsp;</span><span class="number outside">15,622</span></li>
 <li><span class="title">ISS013</span><span class="bar" style="width:139px;">&nbsp;</span><span class="number outside">74,397</span></li>
 <li><span class="title">ISS014</span><span class="bar" style="width:14px;">&nbsp;</span><span class="number outside">7,906</span></li>
 <li><span class="title">ISS015</span><span class="bar" style="width:39px;">&nbsp;</span><span class="number outside">20,883</span></li>
 <li><span class="title">ISS016</span><span class="bar" style="width:36px;">&nbsp;</span><span class="number outside">19,550</span></li>
 <li><span class="title">ISS017</span><span class="bar" style="width:20px;">&nbsp;</span><span class="number outside">11,023</span></li>
 <li><span class="title">ISS018</span><span class="bar" style="width:52px;">&nbsp;</span><span class="number outside">27,870</span></li>
 <li><span class="title">ISS019</span><span class="bar" style="width:20px;">&nbsp;</span><span class="number outside">11,143</span></li>
 <li><span class="title">ISS020</span><span class="bar" style="width:47px;">&nbsp;</span><span class="number outside">25,258</span></li>
 <li><span class="title">ISS021</span><span class="bar" style="width:48px;">&nbsp;</span><span class="number outside">25,884</span></li>
 <li><span class="title">ISS022</span><span class="bar" style="width:166px;">&nbsp;</span><span class="number outside">88,932</span></li>
 <li><span class="title">ISS023</span><span class="bar" style="width:84px;">&nbsp;</span><span class="number outside">45,212</span></li>
 <li><span class="title">ISS024</span><span class="bar" style="width:9px;">&nbsp;</span><span class="number outside">5,270</span></li>
 <li><span class="title">ISS025</span><span class="bar" style="width:22px;">&nbsp;</span><span class="number outside">12,101</span></li>
 <li><span class="title">ISS026</span><span class="bar" style="width:46px;">&nbsp;</span><span class="number outside">24,662</span></li>
 <li><span class="title">ISS027</span><span class="bar" style="width:50px;">&nbsp;</span><span class="number outside">26,766</span></li>
 <li><span class="title">ISS028</span><span class="bar" style="width:58px;">&nbsp;</span><span class="number outside">31,044</span></li>
 <li><span class="title">ISS029</span><span class="bar" style="width:60px;">&nbsp;</span><span class="number outside">32,056</span></li>
 <li><span class="title">ISS030</span><span class="bar" style="width:489px;">&nbsp;</span><span class="number outside">261,166</span></li>
 <li><span class="title">ISS031</span><span class="bar" style="width:271px;">&nbsp;</span><span class="number outside">144,718</span></li>
 <li><span class="title">ISS032</span><span class="bar" style="width:17px;">&nbsp;</span><span class="number outside">9,409</span></li>
 <li><span class="title">ISS033</span><span class="bar" style="width:21px;">&nbsp;</span><span class="number outside">11,356</span></li>
 <li><span class="title">ISS034</span><span class="bar" style="width:97px;">&nbsp;</span><span class="number outside">52,173</span></li>
 <li class="total"><span class="title">Total:</span><strong>1,129,177</strong></li>
</ul>


One more thing we can do is add a map underneath to see exactly how the photos line up:


Here you can see that the ISS stays between about 50&deg; and -50&deg; latitude as it orbits the Earth
The [inclination](http://en.wikipedia.org/wiki/Orbital_inclination) of the orbit
of the station is in fact 51.6&deg;. This is high enough that it can communicate
with ground stations in Russia, while low enough that vehicles launching from the USA
can reach it.

Since it's hard to see the overlapped colors in the above image here is a
collection maps with the photos from each mission mapped separately:

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
