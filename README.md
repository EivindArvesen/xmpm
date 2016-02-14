# xpm

[![docs][docs-image]][docs-url]
[![travis][travis-image]][travis-url]
[![coveralls][coveralls-image]][coveralls-url]
[![license][license-image]][license-url]
[docs-image]: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat
[docs-url]: http://xpm.readthedocs.org
[travis-image]: https://api.travis-ci.org/eivind88/xpm.svg
[travis-url]: https://travis-ci.org/eivind88/xpm
[coveralls-image]: https://coveralls.io/repos/eivind88/xpm/badge.svg?branch=master&service=github
[coveralls-url]: https://coveralls.io/github/eivind88/xpm
[license-image]: http://img.shields.io/badge/license-BSD3-brightgreen.svg
[license-url]: https://github.com/eivind88/xpm/blob/master/LICENSE.txt

![Icon](res/small_icon.png)

### WORK IN PROGRESS
**This software is not yet finished, and might not be usable in its present state.**

xpm is a cross-platform (meta-)package manager.

## Installation
Binaries can be downloaded from the [releases](https://github.com/eivind88/xpm/releases) page.

As xpm is under rapid development, these may be outdated, and infrequently updated.

Alternatively, you can install xpm in one of the following ways:

<!-- Brew cask distribution -->

### Automatic environment setup
If you don't have Python installed, already have the [Anaconda Python distribution](https://store.continuum.io/cshop/anaconda/) installed or don't have any preference regarding Python distribution, the included `setup.sh` can set up a development environment for you.
Running

```shell
bash dev/setup.sh
```

will check if the default Anaconda Python path exists, and download and install the latest [miniconda distribution](http://conda.pydata.org/miniconda.html) if it doesn't.
The script then creates a [conda](http://conda.pydata.org/docs/) environment from `requirements.txt`.

To start using the environment, activate it with `source activate xpm`.
When you're done, you can deactivate it with `source deactivate`.

The automatic environment setup script should work for modern 64-bit versions of OS X, Linux and Windows (Cygwin).

### Manual environment setup
If you'd like to set up the development manually, the included `requirements.txt` can be used with virtualenv.

With virtualenv, this should go something like

```shell
pip install -r requirements.txt
```

once you have created and activated an environment.

If you'd like to build the application yourself, you will also need to install PyInstaller manually:

```shell
pip install git+https://github.com/pyinstaller/pyinstaller.git@develop
```

### Distribution
To prepare the application for distribution after setting up the development environment, run:

```shell
bash dev/build.sh
```

This script runs PyInstaller on the included ```main.spec```,
and outputs a packaged application in a newly created folder ```dist```.

At present, only OS X builds are officially supported.

### Tests
To run the project unit tests, run ```nosetests``` from the project root, or run:

```shell
bash dev/run-tests.sh
```

to run the tests with coverage.

### Documentation
The documentation can be built locally via sphinx by running ```sphinx-apidoc```, or:

```shell
bash dev/generate-docs.sh
```

## Contributions
Feedback is very much appreciated.

If you run into a bug or would like to see a new feature, please open a new issue.

Contributions in the form of code (e.g. implementing new features, bug-fixes) are also appreciated.
Just fork the repo, check out a new branch with an informative name, commit your changes and send a pull request.

In the case of any new dependencies, running

```shell
bash dev/export-env.sh
```

will automatically export your environment and update the ```requirements.txt```, provided you are using a conda env. If you are using virtualenv, you can run

```shell
pip freeze > requirements.txt
```

to do the same.

## License
This software is released under the terms of the 3-clause New BSD License. See the [license](LICENSE.txt) file for details.

[PySide](https://wiki.qt.io/PySide) is released under [LGPL](https://www.gnu.org/copyleft/lesser.html).
Its source code is available on [GitHub](https://github.com/PySide).

The application icon is built upon [Spectacle Flat Icons](https://dribbble.com/shots/2075892-Spectacle-Flat-Icons) and [The Axe](https://dribbble.com/shots/1702501-The-Axe).
