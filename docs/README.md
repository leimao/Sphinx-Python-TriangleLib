
# Triangle Project

## Introduction




## Instructions

### Quick Start

```
$ cd docs/
$ sphinx-quickstart --ext-autodoc --ext-doctest --ext-mathjax --ext-viewcode
Welcome to the Sphinx 3.1.2 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

The project name will occur in several places in the built documentation.
> Project name: trianglelib
> Author name(s): Brandon Rhodes, Lei Mao
> Project release []: 1.1

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: 

Creating file /home/leimao/GitHub/Sphinx-Python-TriangleLib/docs/source/conf.py.
Creating file /home/leimao/GitHub/Sphinx-Python-TriangleLib/docs/source/index.rst.
Creating file /home/leimao/GitHub/Sphinx-Python-TriangleLib/docs/Makefile.
Creating file /home/leimao/GitHub/Sphinx-Python-TriangleLib/docs/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file /home/leimao/GitHub/Sphinx-Python-TriangleLib/docs1/source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

### Create HTML

```
$ cd docs/
$ make clean
$ make html
```


### Create PDF

```
$ cd docs/
$ make clean
$ make latexpdf
```


### Run Doctest

```
$ cd docs/
$ make doctest
Running Sphinx v3.1.2
making output directory... done
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
building [doctest]: targets for 4 source files that are out of date
updating environment: 0 added, 0 changed, 0 removed
looking for now-outdated files... none found
running tests...

Document: guide
---------------
1 items passed all tests:
  10 tests in default
10 tests in 1 items.
10 passed and 0 failed.
Test passed.

Document: tutorial
------------------
1 items passed all tests:
   3 tests in default
3 tests in 1 items.
3 passed and 0 failed.
Test passed.

Document: api
-------------
1 items passed all tests:
   4 tests in default
4 tests in 1 items.
4 passed and 0 failed.
Test passed.

Doctest summary
===============
   17 tests
    0 failures in tests
    0 failures in setup code
    0 failures in cleanup code
build succeeded.

Testing of doctests in the sources finished, look at the results in build/doctest/output.txt.
```


### View Documentation

In another terminal, start a simple HTTP server for viewing the documentation locally.


```
$ cd docs/build/html/
$ python -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

We could then view the documentation in the web browser at [http://0.0.0.0:8000/](http://0.0.0.0:8000/).
