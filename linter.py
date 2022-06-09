"""Robocop linter for Sublime Text."""
from SublimeLinter.lint import PythonLinter


class Robocop(PythonLinter):
    """Robocop linter."""

    cmd = 'robocop'
    # regex = r'(.*)\:(\d+)\:(\d+) \[(W|I|E)\] (\d+) (.*)'
    regex = '(?P<filename>.*)\:(?P<line>\d+)\:(?P<col>\d+) \[(?P<warning>W|I|)?(?P<error>E)?\] (?P<code>\d+) (?P<message>.*)'
    multiline = False
    defaults = {
        'selector': 'source.robot'
    }

'''
Name    | Description                                   | example
--------|-----------------------------------------------|-----------------------
line    | The line number on which the problem occurred | 16
col     | The column number where the error occurred    | 1
message | The description of the problem                | Keyword name (to eol)
error   | the error will be marked as an error by       | [E]
warning | the error will be marked as a warning by      | [W] or [I]
code    | The corresponding error code given            | 0302



/Users/rtownshend/repos/timesheet-e2e/TestCases/gherkin_login.robot:16:1 [W] 0302 Keyword name 'When User 'rtownshend' Logs In With Password 'a'' does not follow case convention (wrong-case-in-keyword-name)

/Users/rtownshend/repos/timesheet-e2e/TestCases/gherkin_login.robot:28:1 [I] 0302 Keyword name 'Input password' does not follow case convention (wrong-case-in-keyword-name)

/Users/rtownshend/repos/timesheet-e2e/TestCases/timesheet_login.robot:11:1 [E] 0313 Test case name should not be empty (test-case-name-is-empty)

# cmd = 'pyflakes'
# regex = r'''(?x)
#     ^(?P<filename>.+?):(?P<line>\d+):((?P<col>\d+):?)?\s
#     # The rest of the line is the error message.
#     # Within that, capture anything within single quotes as `near`.
#     (?P<message>[^\'\n\r]*(?P<near>\'.+?\')?.*)
# '''

'''


