![Watson Logo](https://tailordev.github.io/Watson/img/logo-watson-600px.png)

![Build Status][Build-Status] ![PyPI Latest Version][PyPI-Latest-Version] ![Requires IO][Requires-io]

This is my personal fork of Watson that I maintain. I used Watson for several months and really enjoyed it, 
however there were some features that I really wanted. One of the main things I wanted was the ability to add comments to
my logged time. Luckily one of the maintainers actually had a pull request to add such a thing!
When I looked further into the PR, I saw that it had been open for over a year, so who knows when it will actually be merged into master. 

This fork contains the following PR's from the upstream branch:


* __#115__: Refactor 'watson.frames' @SpotlightKid
* __#119__: Add log messages to frames @SpotlightKid
* __#140__: Make formatting styles configurable @SpotlightKid

Other changes:

* README rewritten in Markdown (personal preference)


From the original documentation on Watson:

> Watson is here to help you manage your time. You want to know how
> much time you are spending on your projects? You want to generate a nice
> report for your client? Watson is here for you.

Wanna know what it looks like? Check this below.

![Watson screenshot][Watson-screenshot]

Nice isn't it?

# Quick start #

## Installation ##

On OS X, the easiest way to install **watson** is using [Homebrew](http://brew.sh/):

``` bash
$ brew update && brew install watson
```

On other platforms, install **watson** using pip:

``` bash
$ pip install td-watson
```

If you need more details about installing watson, please refer to the [documentation](https://tailordev.github.io/Watson).

## Usage ##


Start tracking your activity via:

``` bash
$ watson start world-domination +cats
```
With this command, you have started a new **frame** for the *world-domination* project with the *cat* tag. That's it.

Now stop tracking you world domination plan via:

``` bash
$ watson stop
Project world-domination [cat] started 8 minutes ago (2016.01.27 13:00:28+0100)
```

You can log your latest working sessions (aka **frames**) thanks to the ```log``` command:

``` bash
$ watson log
Tuesday 26 January 2016 (8m 32s)
      ffb2a4c  13:00 to 13:08      08m 32s   world-domination  [cat]
```

Please note that, as [the report command](https://tailordev.github.io/Watson/user-guide/commands/#report), the ```log``` command comes with projects, tags and dates filtering.

To list all available commands, either [read the documentation](https://tailordev.github.io/Watson) or use:

``` bash
  $ watson help
```

# Contributor Code of Conduct #


If you want to contribute to this project, please read the project [Contributor Code of Conduct](https://tailordev.github.io/Watson/contributing/coc/)

# License #

Watson is released under the MIT License. See the bundled LICENSE file for
details.

[Build-Status]: https://travis-ci.org/TailorDev/Watson.svg?branch=master
[PyPI-Latest-Version]: https://img.shields.io/pypi/v/td-watson.svg
[Requires-io]: https://requires.io/github/TailorDev/Watson/requirements.svg?branch=master
[Watson-screenshot]: https://tailordev.github.io/Watson/img/watson-demo.gif

