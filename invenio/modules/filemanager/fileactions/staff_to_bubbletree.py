# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013, 2014 CERN.
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

"""FileManager tranform action."""

import csv
import json
import requests

from six import StringIO

from ..utils import FileManagerAction


class FileAction(FileManagerAction):
    """File Action plugin implementation."""

    accepted_mimetypes = ['text/plain', 'text/csv']
    response_mimetype = 'application/json'

    def action(self, *args, **kwargs):
        """Transforms a CSV file to a JSON file."""
        files = kwargs.get('files')
        name = kwargs['params'].get('name', 'top-category')
        label = kwargs['params'].get('label', 'Top Category')
        result = {
            'name': name,
            'label': label,
        }
        total_amount = 0
        types = []
        for filename in files:
            response = requests.get(filename)
            csvreader = csv.reader(StringIO(response.content))
            header = csvreader.next()
            category = {
                'name': header[0],
                'label': header[0],
                'amount': header[1],
            }
            total_amount += int(header[1])
            children = []
            for row in csvreader:
                child = {
                    'name': row[0],
                    'label': row[0],
                    'amount': row[1],
                }
                children.append(child)
            category['children'] = children
            types.append(category)
        result['amount'] = total_amount
        result['children'] = types
        return json.dumps(result)
