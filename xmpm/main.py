#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""A cross platform meta-package manager"""
__author__ = "Eivind Arvesen"
__copyright__ = "Copyright (c) 2016, Eivind Arvesen. All rights reserved."
__credits__ = ["Eivind Arvesen"]  # Bugfixers, suggestions etc.
__license__ = "BSD-3"  # LGPL/GPL3/BSD/Apache/MIT/CC/C/whatever
__version__ = "0.0.1 Alpha"  # "Alpha", "Beta", ""
__maintainer__ = "Eivind Arvesen"
__email__ = "eivind.arvesen@gmail.com"
__status__ = "Prototype"  # Prototype/Development/Production
__date__ = "2016/02/14 17:30:23 CET"
__todo__ = [
    ""
]
__bug__ = "None"

# Copyright (c) 2016 Eivind Arvesen. All rights Reserved.

import argparse
import json
import os
import platform
import subprocess
import sys


class Xmpm(object):
    """Docstring goes here."""

    def __init__(self):
        """Parse args, call appropriate function for each package."""
        parser = argparse.ArgumentParser(
            description='Description.', prog='PROG')
        parser.add_argument(
            'action', choices=('install', 'remove', 'upgrade', 'clean'))
        parser.add_argument(
            'name', nargs='*', help='name(s) of software to manipulate)')

        args = parser.parse_args()

        if platform.system() == 'Darwin':
            self.os_name = 'osx'
            self.os_version = platform.mac_ver()[0]
        elif platform.system() == 'Linux':
            self.os_name = str.lower(platform.system())
            self.os_version = platform.linux_distribution()[0]
        elif platform.system() == 'Windows':
            self.os_name = str.lower(platform.system())
            self.os_version = platform.win32_ver()[0]

        script_path = os.path.dirname(os.path.realpath(__file__))
        packages = os.path.realpath(script_path + os.sep + 'packages')
        os_providers = os.path.realpath(
            script_path + os.sep + 'providers' + os.sep + 'os' + os.sep +
            self.os_name)
        lang_providers = os.path.realpath(
            script_path + os.sep + 'providers' + os.sep + 'lang')

        for name in args.name:
            # test if software is already installed
            finish_status = install_status = subprocess.call(
                ["which", name], stderr=subprocess.STDOUT,
                stdout=subprocess.PIPE)

            if finish_status == 0:
                print 'Could not', args.action, name

            else:

                while finish_status == 1:
                    xmpm_package = packages + os.sep + name + '.json'

                    if os.path.isfile(xmpm_package):
                        if self.xmpmInstall(xmpm_package):
                            finish_status = install_status = 0

                    else:
                        os_managers = []  # list apropriate managers
                        for manager in os_managers:
                            manager_content = []  # parse json
                            if subprocess.call(
                                ["which", manager_content['bin']], stderr=subprocess.STDOUT,
                                stdout=subprocess.PIPE):
                                if self.osInstall(name):
                                    finish_status = install_status = 0

                        lang_managers = []  # list apropriate managers
                        for manager in lang_managers:
                            manager_content = []  # parse json
                            if subprocess.call(
                                ["which", manager_content['bin']], stderr=subprocess.STDOUT,
                                stdout=subprocess.PIPE):
                                if self.langInstall(name):
                                    finish_status = install_status = 0

                    else:
                        print 'Could not', args.action, name
                        finish_status = 0

    def xmpmInstall(self, package):
        """Install via xmpm-package."""
        with open(package, 'r') as f:
            read_data = f.read()
        recipe = json.loads(read_data)

        # command = recipe['platforms'][self.os_name][args.action]
        print recipe['platforms'][self.os_name]
        # perform command

    def osInstall(self, package, provider=None):
        """Install via os-level package manager."""
        pass

    def langInstall(self, package, provider=None):
        """Install via language-level package manager."""
        pass


if __name__ == '__main__':
    app = Xmpm()
