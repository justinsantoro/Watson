![Watson Logo](https://tailordev.github.io/Watson/img/logo-watson-600px.png)

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
* Show frame message in ```log``` command


## Roadmap ##

Below is a roadmap of features that I am wanting to add. While this fork should always have the same functionality as the upstream version,
there are some things that I would like, that I don't see the original version adding anytime soon.

* Stevedore based plugin system for extensible backend system
=======


From the original documentation on Watson:

> Watson is here to help you manage your time. You want to know how
> much time you are spending on your projects? You want to generate a nice
> report for your client? Watson is here for you.

Wanna know what it looks like? Check this below.

![Watson screenshot][Watson-screenshot]

Nice isn't it?

# Quick start #

## Installation ##

Since this is a personal fork, the best (and only) way to install is from the source. You can do so with the following command:

``` bash
python setup.py install
```

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

You can add a log message when you stop a project through the ```--message``` or ```-m``` flag. For example:
```
$ watson stop -m "Worked on harvesting catnip"
```

You can log your latest working sessions (aka **frames**) thanks to the ```log``` command:

``` bash
$ watson log
Tuesday 26 January 2016 (8m 32s)
      ffb2a4c  13:00 to 13:08      08m 32s   world-domination  [cat]
      ffb2a4c  13:08 to 13:20      08m 32s   world-domination  [cat] - Get all the catnip!
```

Please note that, as [the report command](https://tailordev.github.io/Watson/user-guide/commands/#report), the ```log``` command comes with projects, tags and dates filtering.

To list all available commands, either [read the documentation](https://tailordev.github.io/Watson) or use:

``` bash
  $ watson help
```

## Roadmap ##

Below is a roadmap of features that I am wanting to add. While this fork should always have the same functionality as the upstream version,
there are some things that I would like, that I don't see the original version adding anytime soon.

* Stevedore based plugin system for extensible backend system

# Contributor Code of Conduct #


If you want to contribute to this project, please read the project [Contributor Code of Conduct](https://tailordev.github.io/Watson/contributing/coc/)

# License #

Watson is released under the MIT License. See the bundled LICENSE file for
details.

[Watson-screenshot]: https://tailordev.github.io/Watson/img/watson-demo.gif

