"""Robocop linter for Sublime Text."""
from SublimeLinter.lint import PythonLinter


# filename, line, col, warning, error, code, message
# PATTERN = r'[\w\/\-]*\/(?P<filename>\w+\.\w+)\:(?P<line>\d+)\:(?P<col>\d+) \[(?P<warning>W|I|)?(?P<error>E)?\] (?P<code>\d+) (?P<message>.*)'  # noqa
PATTERN = r"^.+?\:(?P<line>\d+)\:(?P<col>\d+) \[(?P<warning>W|I|)?(?P<error>E)?\] (?P<code>\d+) (?P<message>.*)"  # noqa


class Robocop(PythonLinter):
    """Robocop linter."""

    cmd = 'robocop'
    # regex = r'(.*)\:(\d+)\:(\d+) \[(W|I|E)\] (\d+) (.*)'
    regex = PATTERN
    multiline = False
    defaults = {
        'selector': 'source.robot'
    }
