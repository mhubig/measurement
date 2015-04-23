### Prerequisites

In order to use the includet iPython Notebooks, you need to install [Python3](https://www.python.org/)
and [virtualenv](https://virtualenv.pypa.io/en/latest/).

    # On a mac this can easily be done with homebrew
    $ brew install python3
    $ pip install virtualenv
    $ virtualenv env
    $ source env/bin/activate

### Setup & Start

    (env)$ pip install -r requirements.txt
    (env)$ ipython notebook