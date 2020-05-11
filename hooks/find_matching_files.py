# Copyright (c) 2018 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Hook that gets executed when searching for files that match
a glob-style pattern.
"""

import glob

from sgtk import Hook


class FindMatchingFiles(Hook):

    def execute(self, glob_str, **kwargs):
        """
        Return a list of file paths matching the glob string.

        The default implementation uses glob.iglob to search for files

        :param glob_str: A glob style matching pattern
        :type glob_str: str
        """
        return glob.iglob(glob_str)
