#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Administrator
# Copyright (c) 2016 Administrator
#
# License: MIT
#

"""This module exports the Ss plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Ss(NodeLinter):
    """Provides an interface to ss."""

    syntax = ''
    cmd = 'ss'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = r''
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'

