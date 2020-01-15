#! /usr/bin/env python3

"""
Performs pylint on all python files in the project repo's test directory (recursively).

This script is meant to be run from the CI.
"""

import os

def pylint_all_filenames(rootdirs):
    """
    Performs pylint on all python files within given root directory (recursively).
    """
    filenames = []
    for rootdir in rootdirs:
        for rootpath, _, filenames_w in os.walk(rootdir):
            for filename in filenames_w:
                if filename.endswith('.py'):
                    filenames.append(os.path.join(rootpath, filename))

    failed = []
    for filename in filenames:
        cmdline = "pylint \"{}\"".format(filename)
        exit_code = os.system(cmdline)
        if exit_code != 0:
            failed.append(filename)

    if failed:
        raise RuntimeError("pylint failed on {}/{} files.".format(len(failed), len(filenames)))

if __name__ == "__main__":
    pylint_all_filenames([
        os.path.abspath(os.path.dirname(__file__) + "/../scripts"),
        os.path.abspath(os.path.dirname(__file__) + "/../test")])
