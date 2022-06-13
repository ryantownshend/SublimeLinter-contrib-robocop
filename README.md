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

Name    | Description                                   | example
--------|-----------------------------------------------|-----------------------
line    | The line number on which the problem occurred | 16
col     | The column number where the error occurred    | 1
message | The description of the problem                | Keyword name (to eol)
error   | the error will be marked as an error by       | [E]
warning | the error will be marked as a warning by      | [W] or [I]
code    | The corresponding error code given            | 0302

```text
/Users/rtownshend/repos/timesheet-e2e/TestCases/gherkin_login.robot:16:1 [W] 0302 Keyword name 'When User 'rtownshend' Logs In With Password 'a'' does not follow case convention (wrong-case-in-keyword-name)

/Users/rtownshend/repos/timesheet-e2e/TestCases/gherkin_login.robot:28:1 [I] 0302 Keyword name 'Input password' does not follow case convention (wrong-case-in-keyword-name)

/Users/rtownshend/repos/timesheet-e2e/TestCases/timesheet_login.robot:11:1 [E] 0313 Test case name should not be empty (test-case-name-is-empty)
```

```text
cmd = 'pyflakes'
regex = r'''(?x)
    ^(?P<filename>.+?):(?P<line>\d+):((?P<col>\d+):?)?\s
    # The rest of the line is the error message.
    # Within that, capture anything within single quotes as `near`.
    (?P<message>[^\'\n\r]*(?P<near>\'.+?\')?.*)
'''
```
