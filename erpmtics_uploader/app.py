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
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

#
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


logger.debug("Test")

import httplib2
import pprint
import sys

#print sys.modules

#fix ImportError: No module named appengine.api
#I don't understand why, beacuse on my app on https://erpmticspy-dev.appspot.com/
# i use without problem
#=============================================================================
def load_sdk_google():
  # Try to import the appengine code from the system path.
  try:
    from google.appengine.api import apiproxy_stub_map
  except ImportError, e:
    # force removing 'google' package
    if sys.modules.has_key('google'):    
        del sys.modules['google']        #<--- fix
    #sys.path.insert(0, '/opt/google-appengine-python')

    # Make sure App Engine APK is available
    sys.path.append('/opt/google-appengine-python') #test import form 
    import dev_appserver
    dev_appserver.fix_sys_path()

    """
    import dev_appserver
    sys.path = dev_appserver.EXTRA_PATHS + sys.path 
    """
    # Not on the system path. Build a list of alternative paths where it may be.
    # First look within the project for a local copy, then look for where the Mac
    # OS SDK installs it.

load_sdk_google()




#http://code.google.com/p/gaeunit/issues/detail?id=15#c1
#This fixed my memcache "No api proxy found" errors.
#Run server local for evit No api proxy found 
def clear_datastore():
    from google.appengine.api import apiproxy_stub_map, datastore_file_stub

    if 'datastore' in apiproxy_stub_map.apiproxy._APIProxyStubMap__stub_map:
        del apiproxy_stub_map.apiproxy._APIProxyStubMap__stub_map['datastore']

    if 'datastore_v3' in apiproxy_stub_map.apiproxy._APIProxyStubMap__stub_map:
        del apiproxy_stub_map.apiproxy._APIProxyStubMap__stub_map['datastore_v3']

    stub = datastore_file_stub.DatastoreFileStub('YOUR_APP_ID_HERE', '/dev/null','/dev/null')
    apiproxy_stub_map.apiproxy.RegisterStub('datastore', stub)

#clear_datastore()
"""
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.api import apiproxy_stub_map
from google.appengine.api import datastore_file_stub
from google.appengine.api import mail_stub
from google.appengine.api import urlfetch_stub
from google.appengine.api import user_service_stub 
"""


#https://developers.google.com/appengine/docs/python/memcache/usingmemcache
from google.appengine.api import memcache

# Add a value if it doesn't exist in the cache, with a cache expiration of 1 hour.
memcache.add(key="weather_USA_98105", value="raining", time=3600)

# Set several values, overwriting any existing values for these keys.
memcache.set_multi({ "USA_98105": "raining",
                     "USA_94105": "foggy",
                     "USA_94043": "sunny" },
                     key_prefix="weather_", time=3600)

# Atomically increment an integer value.
memcache.set(key="counter", value=0)
memcache.incr("counter")
memcache.incr("counter")
memcache.incr("counter")

sys.exit()

#from google.appengine import *
from oauth2client.client import OAuth2WebServerFlow
from apiclient.discovery import build
from oauth2client.appengine import AppAssertionCredentials

# import pkgutil
# import google
# google.__path__ = pkgutil.extend_path(google.__path__, google.__name__)

# The API Key of the project.
# Create the API keys and/or OAuth 2.0 credentials 
#that client applications will use to identify themselves in API calls.
API_KEY = ''

def createDriveService():
  """Builds and returns a Drive service object authorized with the
  application's service account.

  Returns:
    Drive service object.
  """
  credentials = AppAssertionCredentials(
      scope='https://www.googleapis.com/auth/drive')
  http = httplib2.Http()
  http = credentials.authorize(http)

  return build('drive', 'v2', http=http, developerKey=API_KEY)

createDriveService()
sys.exit()
def main(args=sys.argv):
    """The main function for the erpmtics_agent program."""
    logger.debug(args)

    try:
        logger.debug("Init the app")

        id = "...@developer.gserviceaccount.com" # from google API console - convert private key to base64 or load from file
        #key = base64.b64decode(...)

        credentials = SignedJwtAssertionCredentials(id, key, scope='https://www.googleapis.com/auth/drive')
        credentials.authorize(httplib2.Http())

        gauth = GoogleAuth()
        gauth.credentials = credentials
        drive = GoogleDrive(gauth)
        sys.exit()
        """
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'
        file1.SetContentString('Hello World!') # Set content of the file from given string
        file1.Upload()
        """
    except ImportError:
        raise
    except Exception, e:
        raise    

if __name__ == '__main__':
    main()    