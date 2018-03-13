# K-means Clustering Implementation


## Introduction

This module presents different implementations of K-means clustering algorithms in pure python :
* The first one is based on Lloyd's algorithm.

## Source


The following sources were used to write the implementations:

* https://en.wikipedia.org/wiki/K-means_clustering


## Motivation

The purpose of this exercice is to gain a better understanding of K-means algorithms.

It is also a valuable exercice to practice programming in python language.


## Gained insights

### Algorithm

The objective of a K-means algorithm is to cluster a set of observation into k groups, called means.

#### Lloyds algorithm

k observations are first randomly chosen from the data set and are used as the initial means [Forgy method]. Then until the k means aren't moving anymore, one first assign to each of the observation the closest mean [using the Euclidan distance] and secondly one each of the means as the centroid of all the observations assigned to that mean.


### Python programing

3 key python concepts were used to implement the different algorihtms :
* While compound statement to iterate the computing of the means until they stop moving.
* Classes and inheritance to model an observation and a mean each inheriting from a List.
* List comprehensions for computation and code clarity purpose.

## Code structure

The code is structured as follow :
```
pyKmeans
├- lloyd.py
└- README.md
```

## Author

Rémi Moise

moise.remi@gmail.com

## Licence

MIT License

Copyright (c) 2018
