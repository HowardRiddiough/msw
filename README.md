# msw-live

## Introduction
msw-live provides a command line tool that can be invoked to create a web based interactive geographic 
visulisation of the current surf forecast. A sample visualisation can be found 
[here](https://howardriddiough.github.io/msw-live/).

The visulisation includes a bubble for every surf spot listed in 
[surf_spots.csv](https://github.com/HowardRiddiough/msw/blob/master/data/surfspots.csv). 
The size of the bubble is determined by the actual wave height and the bubble's color intensity determined by 
the number of solid stars as provided by Magicseaweed. Each bubble can be clicked to show more information 
about the surf spot and it's respective forecast. The idea being to show clearly in one view where the best 
location to surf at a given moment in time is.

msw is powered by Magicseaweed's forecast api, more information can be found 
[here](https://magicseaweed.com/developer/api).

# Installation
Use Python 3.6!

## Install

### Install package inside virtualenv
Create a virtualenv somewhere. For example:

    python -m venv ~/pyvenvs/msw

Activate it:

    source ~/pyvenvs/msw/bin/activate

Now install the package + dependencies + test dependencies (e.g. flake8 and pytest) in editable mode:

    pip install -e ".[test]"

You need to re-activate the virtualenv to make the newly installed executables, such as our own CLI tools 
available in your PATH.

# Contributing code
See [CONTRIBUTING.md](https://github.com/HowardRiddiough/msw-live/blob/master/CONTRIBUTING.md)

# Command Line Tools
Once `msw` is you can invoke the live forecast visualisation as follows: 

    $ mswlive


## Contributors
[HowardRiddiough](https://github.com/HowardRiddiough)