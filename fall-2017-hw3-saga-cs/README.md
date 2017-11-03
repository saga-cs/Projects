# MPCS 51042-2, Python Programming

**Week 3 Assignment**

**Due**: October 15 at 11:59pm CT

For each problem, you are to submit a file named `problem<N>.py` where `<N>` is the number of the problem (e.g. `problem1.py`).

## Problem 1: Chainable map/filter/reduce

In some programming languages (e.g., JavaScript), map, filter, and reduce are effectively methods of iterable types. For this problem, you are to create a sub-class of a normal Python list that has map, filter, and reduce methods that can be chained.

### Specifications

- The class should be named `FunctionalList` and should inherit from the built-in `list` class.
- The `map` method should accept a function as its only argument  and return a `FunctionalList` that results from applying a `map` with the specified function on the original sequence.
- The `filter` method should accept a function as its only argument and return a `FunctionalList` that results from applying a `filter` with the specified function on the original sequence.
- The `reduce` method should accept a function (of two arguments) as its only argument and return the object that results from applying `functools.reduce` with the specified function on the original sequence.

### Example Interaction

```pycon
>>> x = FunctionalList(range(10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x.map(lambda x: x**2)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> x.map(lambda x: x**2)
     .filter(lambda x: x > 10)
[16, 25, 36, 49, 64, 81]
>>> x.reduce(lambda x, y: x+y)
45
```

## Problem 2: Chicago Public Libraries

In this problem, we're going to continue exploring [open data](https://data.cityofchicago.org) from the City of Chicago, except this time we're going to take advantage of object-oriented programming to build the foundation for a hypothetical "library application".

We have provided you with a CSV file with data on each public library in Chicago including its name, hours of operation, address, website, and location. You are asked to write three classes that will allow a user to easily interact with this data.

### Specifications

The specifications below indicate what classes/methods must be implemented to receive full credit. However, you should feel free to implement helper methods/functions if you find doing so to be useful.

#### Library Class

- Write a class named `Library`, each instance of which represents a single public library in Chicago.
- The `__init__(self, data)` method should receive a dictionary corresponding to a row in the CSV file (see suggested CSV reading code in [City Class](#city-class)). In its body, it should create the following attributes:

  - `self.name` -- name of the library
  - `self.hours` -- hours of operation (it's up to you how you want to store this data)
  - `self.address` -- street address of the library
  - `self.city` -- what city the library is in
  - `self.state` -- what state the library is in
  - `self.zip` -- the ZIP code of the library
  - `self.phone` -- the phone number of the library
  - `self.url` -- the URL for the library's website
  - `self.location` -- the location of the library as an instance of
    `Coordinate` (see specifications in [Coordinate Class](#coordinate-class))

- The `open_website(self)` method should open the website of the library using the [webbrowser.open_new_tab()](https://docs.python.org/3/library/webbrowser.html#webbrowser.open_new_tab) function from the standard library.
- The `is_open(self, time)` method should accept an instance of [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime) and return a boolean indicating whether the library is open.
- The `distance(self, coord)` method should accept an instance of `Coordinate` and return the distance in miles "as the crow flies" from the specified location to the library. See the [description below](#calculating-distance-between-points) for how to calculate distances using latitudes/longitudes.
- The `full_address(self)` method should return a multi-line string (that is, a string with a newline character within it) with the street address, city, state, and ZIP code of the library

#### Coordinate Class

- The `Coordinate` class stores a latitude/longitude pair indicating a physical location on Earth.
- The `__init__(self, latitude, longitude)` method should accept two floats that represent the latitude and longitude in radians.
- `Coordinate.fromdegrees(cls, latitude, longitude)` should be a `@classmethod` that accepts two floats representing the latitude and longitude in degrees and returns an instance of `Coordinate`.
- The `distance(self, coord)` method should accept another instance of `Coordinate` and calculate the distance in miles to it from the current instance.
- The `as_degrees(self)` method should return a tuple of the latitude and longitude in degrees.
- The `show_map(self)` method should open up Google Maps on a web browser with a point placed on the latitude/longitude. The URL you can use for this is `http://maps.google.com/maps?q=<latitude>,<longitude>` where `<latitude>` and `<longitude>` have been replaced by the corresponding decimal degrees.

#### City Class

- The `City` class stores a list of libraries in the city.
- The `__init__(self, filename)` method accepts a filename for the CSV file in which our library data is stored. It should create an attribute called `libraries` that is a list of `Library` instances. To iterate over the rows in the CSV file, you can use the following code:

```python
import csv

with open(filename, 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ...
```

- The `nearest_library(self, coord)` method accepts an instance of `Coordinate` and returns the `Library` instance that is closest to the given coordinates.

#### Calculating distance between points

Since the library locations are given as latitude/longitude coordinates, we need a way to calculate distance given two such pairs. One recommended way to do this is using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula), which is

![Haversine formula](http://latex2png.com/output//latex_864209a59a6d48323e698d6899ee6f06.png)

where `d` is the distance between the two points, `r` is the radius of the Earth (use 3961 miles), ![varphi1](http://latex2png.com/output//latex_a4acc5e8a6c299501f90c28a2ddee69a.png) and ![varphi2](http://latex2png.com/output//latex_7256d5a2af8a38823209a802a4b923ab.png) are the latitudes of the two points in radians, and ![lambda1](http://latex2png.com/output//latex_3b3fb8151d8990dfafdc7954410136ff.png) and ![lambda2](http://latex2png.com/output//latex_e3ca12d2ef3a5f3b30188840c05480c7.png) are the longitudes of the two points in radians. Note that the data you are given is in degrees, not radians, so make sure you [convert it](https://en.wikipedia.org/wiki/Radian#Conversion_between_radians_and_degrees) first.

### Example Interaction

The example below shows an example interaction with these classes at a Python console. Note that for this example, I've implemented a [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__) method in the `Library` and `Coordinate` classes to get a nice string representation (we will discuss this further in week 4); feel free to do the same if you wish.

```pycon
>>> chicago = City('libraries.csv')
>>> chicago.libraries[:5]
[Library(Albany Park),
 Library(Altgeld),
 Library(Archer Heights),
 Library(Austin),
 Library(Austin-Irving)]
>>> [x for x in chicago.libraries if x.name.startswith('N')]
[Library(Near North),
 Library(North Austin),
 Library(North Pulaski),
 Library(Northtown)]
>>> the_bean = Coordinate.fromdegrees(41.8821512, -87.6246838)
>>> chicago.nearest_library(the_bean)
Library(Harold Washington-HWLC)
>>> time = datetime(2017, 10, 9, 20, 30)
>>> [x for x in chicago.libraries if x.is_open(time)]
[Library(Harold Washington-HWLC),
 Library(Sulzer Regional),
 Library(Woodson Regional)]
>>> austin = chicago.libraries[3]
>>> print(austin.full_address())
5615 W. Race Avenue
CHICAGO, IL 60644
>>> austin.location
Coordinate(41.889272153514526, -87.76571186722818)
```