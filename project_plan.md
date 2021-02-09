
# Table of Contents

1.  [References:](#orga5bac3f)
2.  [:](#org742995b)
    1.  [Scenario Generator:](#org852259f)
    2.  [Integrtion of GIS(Geographic Information System) functions:](#orgdf09f57)
    3.  [Packages:](#orgfe9e076)
    4.  [Message Format:](#org6834e74)



<a id="orga5bac3f"></a>

# References:

-   [FLoRa Home Page](https://duckduckgo.com/?q=https://flora.aalto.fi/) [FLoRa Github Repo](https://github.com/mariuszslabicki/flora)
    
        Refer this project for scenrio building, adaptive data rate and other LoRa physical layer specifics.


<a id="org742995b"></a>

# TODO :


<a id="org852259f"></a>

## Scenario Generator:

-   choose location co-ordinates over 10 - 15km range as start and endpoints of the simulation.
-   Density of nodes : high, low and ADR check with message format test.
    
        Note create comma separated vlaue files with node and node attirbutes, nodes are distributed based on the density factor across various locations based on the path in the scenario.
    
    `Attributes` nodeID, Current Location (lat , long), bearing.


<a id="orgdf09f57"></a>

## Integrtion of GIS(Geographic Information System) functions:

[Bearing](https://stackoverflow.com/questions/4308262/calculate-compass-bearing-heading-to-location-in-android) : Caliculate based on the start and end point of the path in the map.

[Calcualate distance between two GPS co-ordinates](https://stackoverflow.com/questions/365826/calculate-distance-between-2-gps-coordinates)

[Calculate the position after a meter increment for the given GPS co-ordinates](https://stackoverflow.com/questions/19803604/increment-meters-to-latitude-and-longitude)

`Solving the problem in  clustering`

Appending one in to the message to stop relaying the message, Only stop if message recieved has &rsquo;0&rsquo; previously, else continue. It is dependent on RSSI (Recieved Signal Strength Indicator) too.
Note to self : Breif the solution as soon as possible.


<a id="orgfe9e076"></a>

## Packages:

[pip install python-baseconv](https://pypi.org/project/python-baseconv/)

[UDP using asyncio](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-transports-protocols) This plays a major role in the communication.


<a id="org6834e74"></a>

## Message Format:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">DevID</th>
<th scope="col" class="org-left">Date And Time</th>
<th scope="col" class="org-left">location</th>
<th scope="col" class="org-left">Hop Count</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">16 Bytes</td>
<td class="org-left">8 Bytes</td>
<td class="org-left">12 Bytes</td>
<td class="org-left">1 Byte</td>
</tr>
</tbody>
</table>

TOTAL = 38 Bytes (yet to figure out a way to reduce the size of the DevID)
Hash of the message is yet to be added to the message once the final size is confirmed.

-   Updated

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">DevID</th>
<th scope="col" class="org-left">Date And Time</th>
<th scope="col" class="org-left">location</th>
<th scope="col" class="org-left">Hop Count</th>
<th scope="col" class="org-left">CRC ( temp )</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">11 Bytes</td>
<td class="org-left">8 Bytes</td>
<td class="org-left">12 Bytes</td>
<td class="org-left">1 Byte</td>
<td class="org-left">8 Bytes</td>
</tr>
</tbody>
</table>

TOTAL = 40 Bytes ( DevID is switched from IPv6 to custom format mentioned below)

`TODO: Hash of the message is yet to be added to the message once the final size is confirmed.`

DevID = Country ( 2 characters ) + State ( 2 Characters ) + Vehicle Type ( Based on no.of tyres ) 11 Bytes
[Random vehilce ID between (0, 999,999,999) is converted to base 36 to reduce the size)]

Maximum: Each category of vehicle in each state of a country can have 999,999,999 vehicles

