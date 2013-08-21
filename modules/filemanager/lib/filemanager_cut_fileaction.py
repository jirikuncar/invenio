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

"""FileManager cut action Plugin"""

class FileAction(FileManagerAction):
    """docstring for Visualizer"""
    name = 'cut'
    accepted_mimetypes = ['text/plain', 'text/csv']
    response_mimetype = 'text/csv'
  
    
  
    def action(self, *args, **kwargs):
        """
        Cut a CSV file from its different columns
        """
        original_file = kwargs.get('files')[0]
        fields = kwargs['params'].getlist('field')
        if not original_file or not fields or len(fields) < 2:
            raise Exception('At least two fields needed!')

        # Check if mimetype is accepted
        mimetype = urllib.URLopener().retrieve(original_file)[1].gettype()
        if mimetype not in self.accepted_mimetypes:
            raise Exception('Not valid mimetype')

        header = urllib2.urlopen(urllib.unquote(original_file)).readline()

        columns_to_remove = [pos for pos, elem in enumerate(header.split(',')) 
        						if elem not in fields]
        result = []
        import csv
        csvreader = csv.reader(urllib2.urlopen(urllib.unquote(original_file)))
        for line in csvreader:
            result.append(','.join([elem for pos, elem in enumerate(line) 
                                if not pos in columns_to_remove]))
        
        return '\n'.join(result)
         
   