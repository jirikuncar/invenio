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
    name = 'cernstafftobubbletree'
    accepted_mimetypes = ['text/plain', 'text/csv']
    response_mimetype = 'application/json'

    def action(self, *args, **kwargs):
        """
        Transforms a CSV file to a JSON file
        """
        files = kwargs.get('files')

        result = {
          'name':'CERN Staff',
          'label':'CERN Staff',
        }
        total_amount = 0
        types = []
        for filename in files:
            csvreader = csv.reader(urllib2.urlopen(urllib.unquote(filename)))
            header = csvreader.next()
            category = {
            'name':header[0],
            'label':header[0],
            'amount':header[1] 
            }
            total_amount += int(header[1])
            countries = []
            for row in csvreader:
                country = {
                    'name':row[0],
                    'label':row[0],
                    'amount':row[1] 
                    }
                countries.append(country)
            category['children'] = countries
            types.append(category)
        result['amount'] = total_amount
        result['children'] = types
        return json.dumps(result)