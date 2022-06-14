"""Robocop linter for Sublime Text."""
from SublimeLinter.lint import PythonLinter


# line, col, warning, error, code, message
PATTERN = r"^.+?\:(?P<line>\d+)\:(?P<col>\d+) \[(?P<warning>W|I|)?(?P<error>E)?\] (?P<code>\d+) (?P<message>.*)"  # noqa


class Robocop(PythonLinter):
    """Robocop linter."""

    cmd = ('robocop', '${file}')
    regex = PATTERN
    multiline = False
    defaults = {
        'selector': 'source.robot'
    }
