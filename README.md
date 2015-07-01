### Prerequisites

In order to use the iPython Notebooks, you need to install [Python3][1] and [virtualenvwrapper][2].

    # On a mac this can easily be done with homebrew and pip
    $ brew install python3
    $ pip install virtualenvwrapper

### Clone & setup a virtualenv

    $ git clone git@github.com:mhubig/measurement.git
    $ cd measurement
    $ mkvirtualenv -a $(pwd) -r requirements.txt -p python3 measurement
    (measurement)$

### Start the iPython notebook server
    (measurement)$ ipython notebook

[1]: https://www.python.org
[2]: http://virtualenvwrapper.readthedocs.org/en/latest/index.html
