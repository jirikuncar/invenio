# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
import urllib, urllib2
from invenio.filemanager_helper import FileManagerAction
import csv

"""FileManager join action Plugin"""

class FileAction(FileManagerAction):
    """docstring for Visualizer"""
    name = 'join'
    accepted_mimetypes = ['text/plain', 'text/csv']
    response_mimetype = 'text/csv'

    def action(self, *args, **kwargs):
        """
        Merges several csv files in one and it is uploaded to Invenio.
        Note: All files must have the same header
        """
        files = kwargs.get('files')
        if not files or len(files) < 2:
            raise Exception('Two o more files needed to join!')

         # Check if mimetype is accepted
        for filename in files:
            mimetype = urllib.URLopener().retrieve(filename)[1].gettype()
            if mimetype not in self.accepted_mimetypes:
                raise Exception('%s has not a valid mimetype', filename)

        # check headers
        header = urllib2.urlopen(urllib.unquote(files[0])).readline()
        for i in range(1, len(files)):
            if urllib2.urlopen(urllib.unquote(files[i])).readline() != header:
                raise Exception('Different Header!')
        
        # joining
        result = []		
        result.append(header[:-1]) #skip the '\n' at the end of the header


        for filename in files:
            csvreader = csv.reader(urllib2.urlopen(urllib.unquote(filename)))
            csvreader.next() #skip header
            for line in csvreader:
                result.append(','.join(line))

        return '\n'.join(result)
