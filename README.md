# Sphinx Python TriangleLib

## Introduction

This is an updated version for [Brandon Rhodes](https://github.com/brandon-rhodes)'s [Sphinx Tutorial](https://github.com/brandon-rhodes/sphinx-tutorial) presented at PyCon every year from 2010 through 2013. The original tutorial was written for Python 2 using Sphinx 1.x. Since Python 3 has entirely replaced Python 2 now, I updated the Sphinx code to make it Python 3 compatible, and added some new components to the code to make it look more close to real projects.

It is strongly recommended to watch Brandon Rhodes's [Sphinx tutorial session](https://www.youtube.com/watch?v=QNHM7q2hLh8) at PyCon 2013, since I have not found any other tutorial videos or blogs are as good as his even though it is year 2020 now. Most of the content he presented is still applicable to Python 3 and the latest Sphinx, and the reStructuredText was covered sufficiently for writing documentations for Sphinx.


## Installation

The `trianglelib` used for the tutorial has no dependency. But for completeness, we added `setuptools` and `sphinx` to our `requirements.txt`. 

To install the dependencies, please run the following command in the terminal.

```
$ pip install -r requirements.txt
```

To install the `trianglelib`, which we would not probably do, please run the following command in the terminal.

```
$ pip install .
```