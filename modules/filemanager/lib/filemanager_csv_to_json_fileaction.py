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
from invenio.filemanager_helper import FileManagerAction
import urllib, urllib2, csv, json

"""FileManager tranform action Plugin"""

class FileAction(FileManagerAction):
    """docstring for Visualizer"""
    name = 'csvtojson'
    accepted_mimetypes = ['text/plain', 'text/csv']
    response_mimetype = 'application/json'

    def action(self, *args, **kwargs):
        """
        Transforms a CSV file to a JSON file
        """
        filename = kwargs.get('files')[0]      

        if not filename: 
            raise Exception('Wrong params!')

        json_file = []
        csvreader = csv.reader(urllib2.urlopen(urllib.unquote(filename)))
        header = csvreader.next()
        for line in csvreader:
            dict_line = {}
            for index in range(len(line)):
                dict_line[header[index]] = line[index]
            json_file.append(dict_line)
        return json.dumps(json_file)  