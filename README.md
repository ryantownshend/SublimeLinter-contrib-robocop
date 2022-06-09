# SublimeLinter-contrib-robocop

This is a template. For "how to make a linter", please check [the HOWTO](HOWTO.md).

-----------------------------------------------------------------

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-robocop.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-robocop)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to
[robocop](https://robocop.readthedocs.io/).

It will be used with files that have the “Robot” syntax.

## Installation

SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `robocop` is installed
on your system.

```shell
pip install robotframework-robocop
```

In order for `robocop` to be executed by SublimeLinter, you must ensure that
its path is available to SublimeLinter.

The docs cover[troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings

- [SublimeLinter settings](http://sublimelinter.readthedocs.org/en/latest/settings.html)
- [Linter settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html)

Additional SublimeLinter-robocop settings:

|Setting|Description    |
|:------|:--------------|
|foo    |Something.     |
|bar    |Something else.|
