#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
# -*- encoding: utf-8 -*-

###############################################################################
# Copyright (C) 2014 Armando Ibarra
# app for upload data to google drive v0.1 alpha - 2014-May-19

# ========================
# Software and source code
# ========================

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. 

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# For details on authorship, see AUTHORS, Licese copy GNU, see LICENSE

#----------------------------------------------------------------------
# main.py
#
# Created: 26/06/2014
#
# Author: Ing. Armando Ibarra - <armandoibarra1@gmail.com>
#----------------------------------------------------------------------

#/usr/share/applications
###############################################################################

#-----------------------|
# Import Python Modules |
#-----------------------|

import sys, os, datetime,time

# Library imports
import signal,subprocess,atexit,tempfile
#optparse is deprecated; you should use argparse in both python2 and python3
import logging
import warnings,errno
import exceptions
import logging,re


#
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


logger.debug("Test")

def main(args=sys.argv):
    """The main function for the erpmtics_agent program."""
    logger.debug(args)

    try:
    	logger.debug("Init the app")
    	gauth = GoogleAuth()
    	gauth.LocalWebserverAuth()
    	drive = GoogleDrive(gauth)

    	file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'
    	file1.SetContentString('Hello World!') # Set content of the file from given string
    	file1.Upload()

    except ImportError:
    	raise
    except Exception, e:
    	raise    