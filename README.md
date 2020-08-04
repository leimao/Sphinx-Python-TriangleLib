# Sphinx Python TriangleLib

## Introduction

This repository is an updated version for [Brandon Rhodes](https://github.com/brandon-rhodes)'s [Sphinx tutorial](https://github.com/brandon-rhodes/sphinx-tutorial) presented at PyCon every year from 2010 through 2013. The original tutorial was written for Python 2 using Sphinx 1.x, and has not been updated since 2013. Since Python 3 has entirely replaced Python 2 now, I have updated the Sphinx code in the tutorial to make it Python 3 compatible, and have added some new components to the code to make it look more close to real projects.

It is strongly recommended to watch Brandon Rhodes's [Sphinx tutorial session](https://www.youtube.com/watch?v=QNHM7q2hLh8) at PyCon 2013, since I have not found any other tutorial videos or blogs are as good as his even though it is year 2020 now. Most of the content he presented is still applicable to Python 3 and the latest Sphinx, and the [reStructuredText](https://docutils.sourceforge.io/rst.html) was covered sufficiently in depth for writing documentations for Sphinx.

This repository would be useful as a reference for documentation with Python 3 and Sphinx, provided that we have taken Brandon Rhodes's Sphinx tutorial session. There is also a short [blog post](https://leimao.github.io/blog/Python-Documentation-Using-Sphinx/) on this on my website.

## Files

```
.
├── docs
│   ├── make.bat
│   ├── Makefile
│   ├── README.md
│   └── source
│       ├── api.rst
│       ├── conf.py
│       ├── examples.rst
│       ├── guide.rst
│       ├── index.rst
│       ├── _static
│       ├── _templates
│       └── tutorial.rst
├── examples
│   ├── 00-create_triangle
│   │   ├── create_triangle.py
│   │   └── README.md
│   └── README.md
├── LICENSE.md
├── README.md
├── requirements.txt
├── setup.py
└── trianglelib
    ├── __init__.py
    ├── shape.py
    ├── tests.py
    └── utils.py
```

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

## Build Documentations

Please check the [`README`](docs/README.md) in [`docs`](docs/) for details.

## Publish Documentations

Go to [Read the Docs](`https://readthedocs.org/dashboard/import/manual/`) and follow the instructions to publish the documentations. The latest version of the documentation of this repo could be found on [TriangleLib's Documentation](https://sphinx-python-trianglelib.readthedocs.io/). Use [GitHub tags](https://github.com/leimao/Sphinx-Python-TriangleLib/tags) for version control on Read the Docs.

## References

* [Brandon Rhodes's Sphinx Tutorial](https://github.com/brandon-rhodes/sphinx-tutorial)
* [Brandon Rhodes's Sphinx Tutorial Session at PyCon 2013](https://www.youtube.com/watch?v=QNHM7q2hLh8)
* [Python Documentation Using Sphinx](https://leimao.github.io/blog/Python-Documentation-Using-Sphinx/)