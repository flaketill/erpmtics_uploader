#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
# -*- encoding: utf-8 -*-

###############################################################################
# Copyright (C) 2014 Armando Ibarra
# $PROPOSE v0.1 alpha - 2014-May-19

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
# Created: 18/06/2014
#
# Author: Ing. Armando Ibarra - <armandoibarra1@gmail.com>
#----------------------------------------------------------------------

#/usr/share/applications
#
#
#
#
#

# This script .. 

# @author: Ing. Armando Ibarra
###############################################################################


from apiclient import errors
from apiclient.http import MediaFileUpload
# ...

def insert_file(service, title, description, parent_id, mime_type, filename):
  """Insert new file.

  Args:
    service: Drive API service instance.
    title: Title of the file to insert, including the extension.
    description: Description of the file to insert.
    parent_id: Parent folder's ID.
    mime_type: MIME type of the file to insert.
    filename: Filename of the file to insert.
  Returns:
    Inserted file metadata if successful, None otherwise.
  """
  media_body = MediaFileUpload(filename, mimetype=mime_type, resumable=True)
  body = {
    'title': title,
    'description': description,
    'mimeType': mime_type
  }
  # Set the parent folder.
  if parent_id:
    body['parents'] = [{'id': parent_id}]

  try:
    file = service.files().insert(
        body=body,
        media_body=media_body).execute()

    # Uncomment the following line to print the File ID
    # print 'File ID: %s' % file['id']

    return file
  except errors.HttpError, error:
    print 'An error occured: %s' % error
    return None